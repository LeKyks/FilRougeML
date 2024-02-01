from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

def charger_donnees(chemin_fichier):
    return pd.read_csv(chemin_fichier)


def clustering_note(df):
    k = 5

    # Sélection des données pour le clustering 
    X = df[['normalized_hours']]

    # Normaliser les données (si nécessaire)
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)

    # Appliquer l'algorithme K-Means
    kmeans = KMeans(n_clusters=k, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_normalized)
    return df

def vis_clusters(df):
    # Visualisation des clusters
    plt.scatter(df['normalized_hours'], df['game'], c=df['cluster'], cmap='viridis')
    plt.title('Clustering des jeux en fonction des temps de jeu normalisés')
    plt.xlabel('Temps de jeu normalisé')
    plt.ylabel('Jeux')
    plt.show()

def check_outliers(df):
    plt.boxplot(df['normalized_hours'], vert=False, showfliers=True)

    # Ajout de titres et de labels
    plt.title('Boîte à moustaches avec outliers')
    plt.xlabel('Temps de jeu normalisé')
    plt.show()

def delete_outliers(df, threshold=1.5):
    """
    Supprime les valeurs aberrantes d'un ensemble de données en utilisant la méthode des écarts interquartiles (IQR).

    :param data: Un tableau NumPy ou une liste contenant les données.
    :param threshold: Le seuil de l'écart interquartile pour déterminer les valeurs aberrantes. Par défaut, il est fixé à 1.5.
    :return: Un tableau NumPy contenant les données sans les valeurs aberrantes.
    """
    # Calcul des quartiles
    q1 = np.percentile(df["normalized_hours"], 25)
    q3 = np.percentile(df["normalized_hours"], 75)

    # Calcul de l'écart interquartile (IQR)
    iqr = q3 - q1

    # Définition des limites pour détecter les valeurs aberrantes
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr

    # Filtrage des valeurs aberrantes
    df["normalized_hours"] = [value for value in df["normalized_hours"] if lower_bound <= value <= upper_bound]

    # Affichage de la boîte à moustaches sans outliers
    plt.boxplot(df['normalized_hours'], vert=False, showfliers=True)
    plt.title('Boîte à moustaches sans outliers')
    plt.xlabel('Temps de jeu normalisé')
    plt.show()
    return df

def map_clusters_to_notes(df):
    # Mapping des clusters à des notes de 1 à 5
    cluster_mapping = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

    # Appliquer le mapping à la colonne 'cluster'
    df['note_user'] = df['cluster'].map(cluster_mapping)
    df=df.drop(columns=['cluster'])
    
    df['note_user'] = [1 if behavior == 'purchase' else note_user for behavior, note_user in zip(df['behavior'], df['note_user'])]
    return df

def note_game(df):
    df_notegame=df.groupby('game')['note_user'].mean().reset_index()
    return df_notegame

def main():
    df=charger_donnees('sum_normalized.csv')
    #check_outliers(df) # On vérifie s'il y a des outliers
    #df=delete_outliers(df)
    df=clustering_note(df)
    #vis_clusters(df)
    df_with_note_users=map_clusters_to_notes(df)
    df_with_note_users.to_csv('games_note_users.csv', index=False)
    df_note_games=note_game(df)
    df_note_games.to_csv('games_note_games.csv', index=False)

if __name__ == "__main__":
    main()