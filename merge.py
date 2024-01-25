from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

def charger_donnees(chemin_fichier):
    return pd.read_csv(chemin_fichier)

def main():
    #nettoyer colonne nom et normaliser pour merge dessus

if __name__ == "__main__":
    main()