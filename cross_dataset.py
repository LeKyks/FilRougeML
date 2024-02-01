import pandas as pd
from fuzzywuzzy import process


def analyze_dataset(df):
    print(df.columns)
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())

def trouver_correspondance(nom, candidats):
    return process.extractOne(nom, candidats, score_cutoff=85)

def main():
    df_sales_pc = pd.read_csv('steam.csv')
    sum_normalized = pd.read_csv('games_note_users.csv')
    
    merged_df = pd.merge(df_sales_pc, sum_normalized,how='inner', left_on='name', right_on='game')
    print(merged_df)
    print(len(merged_df)/len(sum_normalized))

if __name__ == "__main__":
    main()
    
