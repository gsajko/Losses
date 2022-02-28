# %%
# import markdownify
from bs4 import BeautifulSoup
import markdownify
import urllib.request

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


