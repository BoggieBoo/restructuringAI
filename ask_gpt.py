import os
from openai import OpenAI
from tenk_url import name

def ask_gpt(text, cik, year):
    company = name(cik)
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    prompt = (
        """You are a data scraping bot which parses information from Item 7 of an SEC 10-K report.
        Print our questions 1-13, as well as their answers. Be concise. If you cannot answer a question print 'N/A'. The answers should be based on the information passed in.
        Information:
        Company: {company}
        Year: {year}
        CIK: {cik}
        Knowledge: {knowledge}
        1. Company name?
        2. Company year?
        3. CIK?
        4. When was the restructuring plan announced?
        5. What are the management stated reasons (purpose) of restructuring?
        6. What savings does the company anticipate?
        7. What savings did the company accomplish in relation to restructuring performed in prior years?
        8. How much total restructuring charges were recorded?
        9. What is the breakdown (components) of the charges? (severance, lease termination)
        10. How much reduction in employees? (either as a number of employees reduced or as a percentage of the workforce)
        11. Were any facilities closed? If so, which ones? (List countries, states, or any other locations)
        12. Was there a cost reduction? Yes or No.
        13. Did they mention when they want to complete the restructuring? If so, what was the timeline provided?"""
    ).format(knowledge=text, company=company, year=year, cik=cik )
    response = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],model="gpt-4o",)
    return response.choices[0].message.content

