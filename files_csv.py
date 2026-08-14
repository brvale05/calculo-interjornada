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

def get_agosto_dataframe():
    df = pd.read_csv("dados_folha_agosto.csv")

    return df


def write_df_to_csv(df):

    df.to_csv("folha_completa_bruta.csv", index=False)


def write_df_agosto_to_csv(df):

    df.to_csv("folha_completa_agosto_bruta.csv", index=False)


def main():

    df = get_agosto_dataframe()

    write_df_agosto_to_csv(df)

main()
