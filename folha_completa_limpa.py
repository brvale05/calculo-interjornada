import pandas as pd


def get_complete_dataframe():
    df = pd.read_csv("folha_completa_bruta.csv")

    return df


def fix_date(df):
    df["DIA"] = pd.to_datetime(df["DIA"] + "-2026", format="%d-%b.-%Y")

    df["DIA"] = df["DIA"].dt.strftime("%d/%m/%Y")

    return df


def write_names_csv(df):
    df_names = df["NOME"].sort_values(ascending=True).drop_duplicates()
    df_names.to_csv("nomes_bruto.csv", index=False)


def fix_names(df):
    dict_names = {
        "ALBERTO": "ALBERTO MEDEIROS",
        "ALEXANDRE": "ALEXANDRE SILVA",
        "CREYSON": "CREYSON LEMOS",
        "CÍCERO": "CÍCERO LEONARDO",
        "DENILSON": "DENILSON TAVARES",
        "EVALDO JR": "EVALDO JUNIOR",
        "EVANDRO": "EVANDRO SANTOS",
        "FIDELIS": "FIDÉLIS JUNIOR",
        "JEFERSON CABRAL": "JEFFERSON CABRAL",
        "NILSON": "NILSON OLIVEIRA",
        "OSWALDO": "OSWALDO ROSÁRIO",
        "VLADIMIR": "VLADIMIR MEDEIROS",

    }

    df["NOME"] = df["NOME"].str.strip().replace(dict_names)

    df["NOME"] = df["NOME"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    return df


def main():
    df = get_complete_dataframe()
    df = fix_date(df)

    write_names_csv(df)

    df = fix_names(df)

    df.to_csv("folha_completa_limpa.csv", index=False)

    df_names = df["NOME"].sort_values(ascending=True).drop_duplicates()
    df_names.to_csv("nomes_limpo.csv", index=False)

main()
