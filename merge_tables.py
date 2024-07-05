import pandas as pd


def merge(table1, table2):
    # Merge the two DataFrames on 'questionid' and 'question'
    merged_df = pd.merge(table1, table2, on=['id', 'question'], suffixes=('_1', '_2'))

    # Update the 'answer' column in csv1 with the 'answer' column from csv2 where csv1 has 'N/A'
    merged_df['answer'] = merged_df.apply(lambda row: row['answer_2'] if row['answer_1'] == 'N/A' else row['answer_1'], axis=1)

    # Select the required columns
    final_df = merged_df[['id', 'question', 'answer']]

    # Display the final DataFrame
    return final_df
