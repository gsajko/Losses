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
# %%
# credentials = {
#     "type": "service_account",
#     "project_id": SERVICE_ACC,
#     "private_key_id": SERVICE_ACC,
#     "private_key": SERVICE_ACC,
#     "client_email": SERVICE_ACC,
#     "client_id": SERVICE_ACC,
# }
file_path = Path.home().joinpath("secrets/auth.json")
gc = gspread.service_account(file_path)
# gc = gspread.service_account(credentials)
print("done❗️")
