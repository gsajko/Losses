# %%
# import markdownify
from bs4 import BeautifulSoup
import markdownify
import urllib.request

# %%
url = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

# %%
content = markdownify.markdownify(str(soup.find_all("h3")))
content = content[1:-1].replace("\n\n,", "\n\n")
# %%
def save_str_to_md(s, filename):
    with open(filename, "w") as f:
        f.write(s)

save_str_to_md(content, "losses.md")

# %%
