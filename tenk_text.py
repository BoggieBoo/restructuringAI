import os
from sec_api import ExtractorApi

extractorApi = ExtractorApi(os.getenv('SEC_API_KEY'))

# helper function to pretty print long, single-line text to multi-line text
def pprint(text, line_length=100):
  words = text.split(' ')
  lines = []
  current_line = ''
  for word in words:
    if len(current_line + ' ' + word) <= line_length:
      current_line += ' ' + word
    else:
      lines.append(current_line.strip())
      current_line = word
  if current_line:
    lines.append(current_line.strip())
  return('\n'.join(lines))

# extract an item given a 10-K url (default item 7)
def extract_text(url, item='8'):
  return pprint(extractorApi.get_section(url, item, 'text'))
  
# test