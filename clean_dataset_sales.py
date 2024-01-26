import pandas as pd

def analyze_dataset(df):
    print(df.columns)
    print(df.info())

def clean(df):
    df = df.dropna()
    df=df[df['Platform'] == 'PC']
    df['Rank']=range(1, len(df) + 1)
    df=df.drop(['Platform'], axis=1)
    return df

def main():
    df2 = pd.read_csv('vgsales.csv')
    analyze_dataset(df2)
    df_pc = clean(df2)
    analyze_dataset(df_pc)
    df_pc.to_csv('vgsales_pc.csv', index=False)
    

if __name__ == "__main__":
    main()