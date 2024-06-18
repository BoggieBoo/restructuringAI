from tenk_url import find_url
from tenk_text import extract_text
from search import search


def main(cik, year):
    url = find_url(cik, year)
    text = extract_text(url)
    return search(text)

# test
print(main(1018724, 2021))