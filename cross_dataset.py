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
    df_sales_pc = pd.read_csv('vgsales_pc.csv')
    df_steam_clean = pd.read_csv('steam-200k_clean.csv')  
    moyenne_temps_jeu = df_steam_clean.groupby('game')['hours'].mean().reset_index()
    moyenne_temps_jeu['correspondance'] = moyenne_temps_jeu['game'].apply(lambda x: trouver_correspondance(x, df_sales_pc['Name']))
    
    # Diviser la correspondance en deux colonnes (nom et score)
    moyenne_temps_jeu[['correspondant', 'score']] = pd.DataFrame(moyenne_temps_jeu['correspondance'].tolist(), index=moyenne_temps_jeu.index)
    merged_df = pd.merge(df_sales_pc, moyenne_temps_jeu,how='inner', left_on='Name', right_on='correspondant')
    print(merged_df)
    

    # Calculate percentage of rows where "game" and "hours" are empty
    empty_rows_percentage = merged_df[['game', 'hours']].isnull().all(axis=1).mean() * 100
    print(f"Percentage of rows where 'game' and 'hours' are empty: {empty_rows_percentage}%")

if __name__ == "__main__":
    main()
    
