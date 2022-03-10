# %%
import os
import pandas as pd
from pathlib import Path
# %%
# df = pd.read_table("losses_table.md", sep="|").iloc[1:]
# # %%
# # df.drop(['C', 'D'], axis = 1)
# for col in df.columns:
#     if "Unnamed" in col:
#         df.drop(col, axis=1, inplace=True)
# df
# # %%
# df.to_csv("losses_table.csv")

# %%
import gspread
# gc = gspread.service_account("config/auth.json")
file_path = Path.home().joinpath("secrets/auth.json")
gc = gspread.service_account(file_path)
print("done❗️")
