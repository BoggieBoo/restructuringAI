"""
Citation (for header/company data formatting)
SEC Filing Scraper
@author: AdamGetbags
Accessed June 9, 2024
"""

import requests
import pandas as pd

# create request header
header = {'User-Agent': "UC Berkeley bradenleung@berkeley.org"}

# get all companies data
companyTickers = requests.get("https://www.sec.gov/files/company_tickers.json", headers=header)

# create a dataframe of companies, index = CIK (with leading zeros)
companyData = pd.DataFrame.from_dict(companyTickers.json(), orient='index')
companyData['cik_str'] = companyData['cik_str'].astype(str).str.zfill(10)

def name(cik):
    data = pd.DataFrame.from_dict(companyTickers.json(), orient='index').set_index('cik_str')
    return data.loc[cik]

# return 10-K html link from cik and year
def find_url(cik, year, header=header):
    cik2 = str(cik).zfill(10) # fills with leading zeroes
    metadata = requests.get(f'https://data.sec.gov/submissions/CIK{cik2}.json', headers=header)
    forms = pd.DataFrame.from_dict(metadata.json()['filings']['recent'])
    tenks = forms[forms['form']=='10-K'].copy()
    tenks['reportDate'] = pd.to_datetime(tenks['reportDate'].values)
    tenks['year'] = tenks['reportDate'].dt.year
    doc = (tenks[tenks['year'] == year]['primaryDocument'].values[0])
    acc = (tenks[tenks['year'] == year]['accessionNumber'].values[0]).replace("-", "")
    return f'https://www.sec.gov/Archives/edgar/data/{cik2}/{acc}/{doc}'

# test

