import pandas as pd


def merge(table1, table2):
    merged_df = pd.merge(table1, table2, on=['id', 'question'], suffixes=('_1', '_2'))
    merged_df['answer'] = merged_df.apply(lambda row: row['answer_2'] if row['answer_1'] == 'N/A' else row['answer_1'], axis=1)
    final_df = merged_df[['id', 'question', 'answer']]
    return final_df
