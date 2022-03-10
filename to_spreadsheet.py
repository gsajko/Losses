# %%
import os
import pandas as pd
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
SERVICE_ACC = os.environ["SERVICE_ACC"]
gc = gspread.service_account(SERVICE_ACC)
print("done❗️")
# gc = gspread.service_account("config/auth.json")
# %%
# auth_path: str = "config/auth.json"
# auth = json.load(open(auth_path))
# TOKEN = auth["token"]
