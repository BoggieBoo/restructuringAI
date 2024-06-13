"""
Citation (for header/company data formatting)
SEC Filing Scraper
@author: AdamGetbags
Accessed June 9, 2024
"""

import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

# create request header
header = {'User-Agent': "bradenleung@berkeley.org"}

# get all companies data
companyTickers = requests.get("https://www.sec.gov/files/company_tickers.json", headers=header)

# create a dataframe of companies, index = CIK (with leading zeros)
companyData = pd.DataFrame.from_dict(companyTickers.json(), orient='index')
companyData['cik_str'] = companyData['cik_str'].astype(str).str.zfill(10)

def name(cik):
    data = pd.DataFrame.from_dict(companyTickers.json(), orient='index').set_index('cik_str')
    return data.loc[cik]

# return 10-K html link from cik and year
def find(cik, year, header):
    cik2 = str(cik).zfill(10) # fills with leading zeroes
    metadata = requests.get(f'https://data.sec.gov/submissions/CIK{cik2}.json', headers=header)
    forms = pd.DataFrame.from_dict(metadata.json()['filings']['recent'])
    tenks = forms[forms['form']=='10-K'].copy()
    tenks['reportDate'] = pd.to_datetime(tenks['reportDate'].values)
    tenks['year'] = tenks['reportDate'].dt.year
    doc = (tenks[tenks['year'] == year]['primaryDocument'].values[0])
    acc = (tenks[tenks['year'] == year]['accessionNumber'].values[0]).replace("-", "")
    return f'https://www.sec.gov/Archives/edgar/data/{cik2}/{acc}/{doc}'

#print(find(1318605, 2017, header))
url = find(1318605, 2017, header)
print(find(1018724, 2018, header))

# # Fetch the HTML content
# response = requests.get(url)
# html_content = response.text

# # Parse the HTML content
# soup = BeautifulSoup(html_content, 'html.parser')

# # Extract the text content
# text_content = soup.get_text()

# print(text_content)