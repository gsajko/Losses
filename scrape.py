# %%
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
            line_split = line.split("(")
            if len(line_split) > 2:
                vehicle_type = line_split[0] + " (" + line_split[1]
                vehicle_type = vehicle_type.strip()
            else:
                vehicle_type = line_split[0].strip()
            losses[vehicle_type] = {}
            for i in ("destroyed: ", "damaged: ", "abandoned: ", "captured: "):
                if i in line:
                    try:
                        str_splits = (
                            line.split(i)[1]  # split on type
                            .split(",")[0]
                            .replace(")", "")
                            .strip()
                            # if there are still strings after the number
                            .split(" ")[0]
                        )
                        losses[vehicle_type][i.replace(": ", "")] = int(str_splits)
                        
                    except ValueError as e:
                        print(e)
                        raise e
                else:
                    losses[vehicle_type][i.replace(": ", "")] = 0
    df = pd.DataFrame(losses).T
    df["total"] = df.sum(axis=1)
    df.loc["total"] = df.sum()
    df.index.rename("Russian Losses", inplace=True)

    with open("losses_table.md", "w") as f:
        f.write(df.to_markdown())
except Exception as e:
    print("error", e)

# %%
