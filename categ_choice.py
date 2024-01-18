import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

def charger_donnees(chemin_fichier):
    return pd.read_csv(chemin_fichier)

def preparer_donnees(df):
    features = df[['Year', 'Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales','Publisher']]
    features = pd.get_dummies(features, columns=['Genre'])
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    pca = PCA(n_components=2)
    features_pca = pca.fit_transform(features_scaled)
    return features_pca

def appliquer_dbscan(features_pca, eps=0.5, min_samples=5):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    return dbscan.fit_predict(features_pca)

def afficher_clusters(features_pca, labels):
    plt.scatter(features_pca[:, 0], features_pca[:, 1], c=labels, cmap='viridis')
    plt.title('Clustering des jeux vidéo (DBSCAN)')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.show()

def noms_clusters(labels):
    unique_labels = set(labels)
    noms_clusters = {}
    for label in unique_labels:
        noms_clusters[label] = f'Cluster_{label}'
    return noms_clusters

def recommander_jeux(df, labels, cluster_choisi):
    if cluster_choisi == -1:
        jeux_recommandes = df[labels == cluster_choisi]
    else:
        jeux_recommandes = df[labels == cluster_choisi]

    return jeux_recommandes[['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

def main():
    chemin_fichier = 'vgsales_pc.csv'
    df = charger_donnees(chemin_fichier)
    features_pca = preparer_donnees(df)
    labels = appliquer_dbscan(features_pca)

    afficher_clusters(features_pca, labels)

    cluster_choisi = int(input("Choisissez un cluster (ou -1 pour les points considérés comme du bruit) : "))
    jeux_recommandes = recommander_jeux(df, labels, cluster_choisi)

    noms_clusters_dict = noms_clusters(labels)
    nom_cluster_choisi = noms_clusters_dict[cluster_choisi] if cluster_choisi in noms_clusters_dict else "Points considérés comme du bruit"

    print(f"\nJeux recommandés pour {nom_cluster_choisi} :")
    print(jeux_recommandes)

if __name__ == "__main__":
    main()
