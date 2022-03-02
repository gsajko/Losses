# %%
import json
import urllib.request

import markdownify
import pandas as pd
from bs4 import BeautifulSoup

# %%
url = (
    "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
)
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

# %%
content = markdownify.markdownify(str(soup.find_all("h3")))
content = (
    content[1:-1]
    .replace("\n\n,", "\n\n")
    .replace("### ", "")
    .replace("Russia - ", "\n \n ## Russia\n \n ### Russia - ")
    .replace("Ukraine - ", "\n \n ## Ukraine\n \n ### Ukraine - ")
)
# %%
with open("losses.md", "w") as f:
    f.write(content)


with open("losses.html", "w") as f:
    f.write(str(soup))

# %%
try:
    # create markdown table
    losses = {}
    for line in content.split("\n"):

        if "Ukraine" in line:
            break
        if "Russia" in line:
            pass
        elif len(line) > 2:
            vehicle_type = line.split("(")[0].strip()
            losses[vehicle_type] = {}
            for i in ("destroyed: ", "damaged: ", "abandoned: ", "captured: "):
                if i in line:
                    losses[vehicle_type][i.replace(": ", "")] = int(
                        line.split(i)[1].split(",")[0].replace(")", "").strip()
                    )
                else:
                    losses[vehicle_type][i.replace(": ", "")] = 0

    df = pd.DataFrame(losses).T
    df["total"] = df.sum(axis=1)
    df.loc["total"] = df.sum()
    df.index.rename("Russian Losses", inplace=True)
  
    with open("losses_table.md", "w") as f:
        f.write(df.to_markdown())

    # create dict
    df2 = df.drop(["total"], axis=1).sum(axis=1)
    df2.loc["time"] = str(pd.to_datetime("now"))
    df_dict = df2.to_dict()
    try:
        with open("dict_losses.json", "r") as f:
            dict_list = json.loads(f.read())
    except:
        dict_list = []

    dict_list.append(df_dict)

    with open("dict_russian_losses.json", "w") as f:
        json.dump(dict_list, f)
except Exception as e:
    print("error", e)
    pass
