# %%
import os
import pandas as pd
import gspread
from pathlib import Path
import gspread_pandas
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
gs_config = gspread_pandas.conf.get_config(file_name=file_path)
spread = gspread_pandas.Spread('Russian Losses', config=gs_config)
spread.df_to_sheet(df, replace=True, index=False)
# %%
# format first column
file_path = Path.home().joinpath("secrets/auth.json")
gc = gspread.service_account(file_path)
sh = gc.open('Russian Losses')
sheetId = 0
# %%
ranges = [[0,1,500],[1,10, 100]]
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
                    "fields": "pixelSize"
                }
            }
        ]
    }
    res = sh.batch_update(body)

# %%
