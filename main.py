from tenk_url import find_url
from tenk_text import extract_text
from search import search
from ask_gpt import ask_gpt
from datify import datify


def main(cik, year):
    url = find_url(cik, year)
    text = extract_text(url, item='8') #+ extract_text(url, item='8')
    filtered = search(text)
    response = ask_gpt(filtered, cik, year)
    table = datify(response)
    return table

# test
print(main(773840, 2017))