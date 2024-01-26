import pandas as pd

def analyze_dataset(df):
    print(df.columns)
    print(df.info())

def clean(df):
    df = df.dropna()
    df=df.drop(columns=['platforms','appid','steamspy_tags','achievements','release_date','english'], axis=1)
    return df

def main():
    df2 = pd.read_csv('steam.csv')
    analyze_dataset(df2)
    df_clean = clean(df2)
    analyze_dataset(df2)
    df_clean.to_csv('steam_clean.csv', index=False)
    

if __name__ == "__main__":
    main()