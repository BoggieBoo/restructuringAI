import os
from tenk_url import find_url
from tenk_text import extract_text
from search import search
from ask_gpt import ask_gpt
from datify import datify
from merge_tables import merge

def table_from_item(cik, year, item):
    url = find_url(cik, year)
    text = extract_text(url, item)
    filtered = search(text)
    response = ask_gpt(filtered, cik, year)
    table = datify(response)
    return table

# def v_test():
#     version = os.getenv('VERSION')
#     print(version)

def main(cik, year):
    df_7 = table_from_item(cik, year, item='7')
    print(df_7)
    df_8 = table_from_item(cik, year, item='8')
    print(df_8)
    merged = merge(df_7, df_8)
    folder_path = 'company_csv'
    file_name = f'{os.getenv('VERSION')}_{cik}_{year}.csv'
    full_path = os.path.join(folder_path, file_name)
    merged.to_csv(full_path, index=False)
    print(f"File saved to {full_path}")

# test
main(773840, 2017)