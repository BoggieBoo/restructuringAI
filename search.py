import re

# restructuring keywords
test_words = ["dog", "cat", "fish"]
r_words = ["reorganization", "restructuring", "rationalization", "realignment", "repositioning", "layoff", "employee termination", "workforce reduction"]

# creates a pattern based on the inputted words
pattern = re.compile('|'.join(map(re.escape, r_words)), re.IGNORECASE)

# delimiter
sentence = '.'
paragraph = '\n\n' #start of the paragraph symbol

# prompt
prompt = "URL of 10-K: "

# searches inputted text for pattern -> returns pattern
def search(text, pattern=pattern, delimiter=sentence):
    parts = text.split(delimiter)
    matching_parts = [part for part in parts if pattern.search(part)]
    if matching_parts:
        return matching_parts
    else:
        return ["no match"]