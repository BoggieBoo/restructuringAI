from tenk_url import find_url
from tenk_text import extract_text
from search import search
from ask_gpt import ask_gpt


def main(cik, year):
    url = find_url(cik, year)
    text = extract_text(url)
    return ask_gpt(search(text), cik, year)

# test
print(main(773840, 2018))