# stdlib imports
import re
# 3rd party imports
import bs4

doc_path = "sb_raw/OEBPS/Flow_0.html"
f = open(doc_path, "r")
soup = bs4.BeautifulSoup(f)

def run():

    # remove leading indents
    for t in soup("p", style=re.compile("padding-left\s*:\s*\d+\w+\s*;?\s*")):
        del t['style']
    # remove meaningless spans
    for t in soup(lambda x: x.name == "span" and x.attrs == {}):
        t.unwrap()
    # remove empty paragraphs
    for t in soup(lambda x: x.name == "p" and x.contents == []):
        t.decompose()

    # separate document into sections
    # format sections semantically

    print soup.prettify()

run()


