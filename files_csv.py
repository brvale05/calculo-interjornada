import pandas as pd

def get_months_dataframe():
    df_junho = pd.read_csv("dados_folha_junho.csv")
    df_julho = pd.read_csv("dados_folha_julho.csv")

    df = pd.concat([df_junho, df_julho])

    return df

def fix_month(df):
    mask = df["DIA"].astype(str).str.contains("jun", case=False, na=False)

    df.loc[mask, "MES"] = "JUNHO"

    return df

def write_df_to_csv(df):

    df.to_csv("folha_completa_bruta.csv", index=False)

def main():

    df = get_months_dataframe()
    df = fix_month(df)

    write_df_to_csv(df)

main()
