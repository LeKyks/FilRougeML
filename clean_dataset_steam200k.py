import pandas as pd

def analyze_dataset(df):
    print(df.columns)
    print(df.info())

def delete_useless_columns(df):
    df.drop(['0'], axis=1, inplace=True)
    print(df.head())

def get_top_selling_games(df, n):
    top_selling_games = df[df['behavior'] == 'purchase'].groupby('game')['behavior'].count().nlargest(n)
    return top_selling_games

def get_top_played_games(df, n):
    top_played_games = df[df['behavior'] == 'play'].groupby('game')['hours'].sum().nlargest(n)
    return top_played_games

def calul_stats(df):
    df_achats = df[df['behavior'] == 'purchase']
    df_playtime = df[df['behavior'] == 'play']
    playtime_stats = df_playtime.groupby('game')['hours'].agg(['count', 'mean', 'min', 'max', 'sum'])

    # Calculer les statistiques d'achat par jeu
    purchase_stats = df_achats.groupby('game')['behavior'].count()

    # Afficher les statistiques
    print("Statistiques de temps de jeu par jeu:")
    print(playtime_stats)

    print("\nStatistiques d'achat par jeu:")
    print(purchase_stats)
    

    # Usage example
    top_selling_games = get_top_selling_games(df, 10)
    print("Top selling games:")
    print(top_selling_games)

    top_played_games = get_top_played_games(df, 10)
    print("\nTop played games:")
    print(top_played_games)

def get_play_stats(df):
    return df[df['behavior'] == 'play']
     
def main():
    # Read the dataset
    df = pd.read_csv('C:/Users/pierre/OneDrive - Ynov/COURS/M1/Machine learning/Supports de cours/fil rouge/steam-200k.csv', header=None, names=['user_id', 'game', 'behavior', 'hours', '0'])
    # Display the data
    print(df.head())
    

    delete_useless_columns(df)
    df_play=get_play_stats(df)
    # Analyze the dataset
    #analyze_dataset(df)
    # calul_stats(df)
    # Save the dataset
    df_play.to_csv('C:/Users/pierre/OneDrive - Ynov/COURS/M1/Machine learning/Supports de cours/fil rouge/steam-200k_clean.csv', index=False)
    


if __name__ == "__main__":
    main()
