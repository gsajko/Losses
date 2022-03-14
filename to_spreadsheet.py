# %%
import os
from pathlib import Path

import gspread
import gspread_pandas
import pandas as pd

# %%
# convert md to df and csv
df = pd.read_table("losses_table.md", sep="|").iloc[1:]
for col in df.columns:
    if "Unnamed" in col:
        df.drop(col, axis=1, inplace=True)
df.to_csv("losses_table.csv", index=False)
# %%
# send df to google sheet
file_path = Path.home().joinpath("secrets/auth.json")

gc = gspread.service_account(file_path)

sh = gc.open("Russian Losses")
worksheet = sh.worksheet("Sheet1")
sheetId = 0
# first remove old spreadsheet
worksheet.clear()


gs_config = gspread_pandas.conf.get_config(file_name=file_path)
spread = gspread_pandas.Spread("Russian Losses", config=gs_config)
spread.df_to_sheet(df, replace=True, index=False)
# %%

# %%
# formmating
ranges = [[0, 1, 500], [1, 10, 100]]
for columns in ranges:
    body = {
        "requests": [
            {
                "updateDimensionProperties": {
                    "range": {
                        "sheetId": sheetId,
                        "dimension": "COLUMNS",
                        "startIndex": columns[0],
                        "endIndex": columns[1],
                    },
                    "properties": {
                        "pixelSize": columns[2],
                    },
                    "fields": "pixelSize",
                }
            }
        ]
    }
    res = sh.batch_update(body)

worksheet.format("A1:F1", {"textFormat": {"bold": True}})
worksheet.format("A2:F99", {"textFormat": {"bold": False}})
worksheet.format("A1:A1", {"horizontalAlignment": "LEFT"})
worksheet.format(
    "F1:F40",
    {
        "textFormat": {
            "bold": True,
        },
        # "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 0.56},
    },
)
# %%
# add source
worksheet = sh.worksheet("Sheet1")
rows = [
    ".",
    "source:",
    "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html",
]
for row in rows:
    worksheet.append_row([row], table_range="B2:D4")
# %%
