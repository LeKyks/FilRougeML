import pandas as pd


def charger_donnees(chemin_fichier):
    return pd.read_csv(chemin_fichier)

def nettoyer_colonne(df, colonne):
    # Fonction pour nettoyer une colonne spécifique du dataframe
    df[colonne] = df[colonne].str.lower()  # Convertir tous les noms en minuscules
    df[colonne] = df[colonne].str.strip()  # Supprimer les espaces au début et à la fin des noms
    df[colonne] = df[colonne].str.replace(r'[^\w\s]', '')  # Supprimer les caractères non alphanumériques
    df[colonne] = df[colonne].str.replace(r'\([^)]*\)', '')  # Supprimer le contenu entre parenthèses

    return df


def main():
    # Charger les données
    # vgsales_df = charger_donnees('vgsales_pc.csv')
    steam_df = charger_donnees('steam_clean.csv')
    steam_normalized_df = charger_donnees('games_note_users.csv') 

    # Nettoyer les colonnes 'Name' et 'game'
    # vgsales_df = nettoyer_colonne(vgsales_df, 'Name')
    steam_normalized_df = nettoyer_colonne(steam_normalized_df, 'game')
    steam_df = nettoyer_colonne(steam_df, 'name')
    # Effectuer la fusion sur les noms des jeux

    merged_df = pd.merge(steam_normalized_df, steam_df, left_on='game', right_on='name', how='inner')
    print(merged_df)

    # Afficher le résultat ou faire d'autres opérations sur le dataframe fusionné
    merged_df.to_csv('merged.csv', index=False)


if __name__ == "__main__":
    main()
