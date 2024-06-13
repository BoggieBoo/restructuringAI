import re

#restructuring keywords
test_words = ["dog", "cat", "fish"]
r_words = ["reorganization", "restructuring", "rationalization", "realignment", "repositioning", "layoff", "employee termination", "workforce reduction"]

#creates a pattern based on the inputted words
pattern = '|'.join(map(re.escape, test_words))

#delimiter
sentence = '.'
paragraph = '\n\n' #start of the paragraph symbol

#prompt
prompt = "URL of 10-K: "

#searches inputted text for pattern -> returns pattern
def search(pattern, delimiter, string):
    parts = string.split(delimiter)
    matching_parts = [part for part in parts if re.search(pattern, part, re.IGNORECASE)]
    if matching_parts:
        print(matching_parts)
    else:
        print("no match")

def main():
    while True:
        string = input("text: ")
        print(" ")
        search(pattern, sentence, string)
        print(" ")
