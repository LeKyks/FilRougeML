import pandas as pd

def analyze_dataset(df):
    print(df.columns)
    print(df.info())

def get_only_pc_platform(df):
    df = df[df['Platform'] == 'PC']
    df["Rank"]=range(1, len(df) + 1)
    return df

def main():
    df2 = pd.read_csv('C:/Users/pierre/OneDrive - Ynov/COURS/M1/Machine learning/Supports de cours/fil rouge/vgsales.csv')
    analyze_dataset(df2)
    df_pc = get_only_pc_platform(df2)
    df_pc.to_csv('C:/Users/pierre/OneDrive - Ynov/COURS/M1/Machine learning/Supports de cours/fil rouge/vgsales_pc.csv', index=False)
    

if __name__ == "__main__":
    main()