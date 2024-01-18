import pandas as pd

def analyze_dataset(df):
    print(df.columns)
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())


def main():
    df_sales_pc = pd.read_csv('vgsales_pc.csv')
    df_steam_clean = pd.read_csv('')  
    merged_df = pd.merge(df_sales_pc, df_steam_clean, left_on='Name', right_on='game', how='right')
    print(merged_df)
    
    cut_df=merged_df[['rank','user_id', 'game', 'behavior', 'hours', 'Genre']]
    analyze_dataset(cut_df)
    

if __name__ == "__main__":
    main()