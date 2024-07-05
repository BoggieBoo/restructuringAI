import pandas as pd
import re

def datify(input_text):
    blocks = re.split(r'\n(?=\d+\.)', input_text.strip())
    data = []
    for block in blocks:
        question_match = re.match(r'(\d+)\.\s+(.*?)[\?]?\n\s+-\s+(.*)', block, re.DOTALL)
        if question_match:
            questionid = question_match.group(1).strip()
            question = question_match.group(2).strip()
            answer = question_match.group(3).strip()
            data.append({"id": questionid, "question": question, "answer": answer})
    return pd.DataFrame(data, columns=['id', 'question', 'answer'])