from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

def charger_donnees(chemin_fichier):
    return pd.read_csv(chemin_fichier)

def preparer_donnees(df):
    features = df[['Year', 'Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales','Publisher']]
    features = pd.get_dummies(features, columns=['Genre', 'Publisher'])
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    pca = PCA(n_components=2)
    features_pca = pca.fit_transform(features_scaled)
    return features_pca

def normaliser_les_donnees(features):
    scaler = StandardScaler()
    return scaler.fit_transform(features)

def calculate_inertie(df, features_scaled):
    inertia = []
    for n_clusters in range(1, len(df)):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(features_scaled)
        inertia.append(kmeans.inertia_)
    return inertia

def tracer_courbe(inertia):
    plt.plot(range(1, 100), inertia, marker='o')
    plt.xlabel('Nombre de clusters')
    plt.ylabel('Inertie')
    plt.title('Méthode du coude pour trouver le nombre optimal de clusters')
    plt.show()

def main():
    df=charger_donnees('vgsales_pc.csv')
    features=preparer_donnees(df)
    features_scaled=normaliser_les_donnees(features)
    inertia=calculate_inertie(df, features_scaled)
    tracer_courbe(inertia)

if __name__ == "__main__":
    main()