from json.decoder import NaN

import pandas as pd


def get_complete_dataframe():
    df = pd.read_csv("folha_completa_agosto_bruta.csv")

    return df

#
# def separate_string(string):
#
#     vetor = str(string).split("-")
#
#     dia = vetor[0]
#
#     if dia is NaN:
#         pass
#     else:
#         return dia + "/07/2026"


def fix_date(df):
    df["DIA"] = pd.to_datetime(df["DIA"] + "-2026", format="%d-%b.-%Y")

    df["DIA"] = df["DIA"].dt.strftime("%d/%m/%Y")

    return df


def fix_names(df):
    df["NOME"] = df["NOME"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    dict_names = {
        "ALBERTO": "ALBERTO MEDEIROS",
        "ALEXANDRE": "ALEXANDRE SILVA",
        "CREYSON": "CREYSON LEMOS",
        "CICERO": "CICERO LEONARDO",
        "DENILSON": "DENILSON TAVARES",
        "EVALDO JR": "EVALDO JUNIOR",
        "EVANDRO": "EVANDRO S.",
        "FIDELIS": "FIDELIS JUNIOR",
        "JEFERSON CABRAL": "JEFFERSON CABRAL - ARACAJU",
        "NILSON": "NILSON OLIVEIRA",
        "OSWALDO": "OSWALDO ROSARIO",
        "VLADIMIR": "VLADIMIR MEDEIROS",
        "CLAUDIO ROBERTO": "CLAUDIO R.",
        "MARCIO COSTA": "MARCIO COSTA - ARACAJU",
        "EVANDRO SANTOS": "EVANDRO S.",
        "JEFFERSON CABRAL": "JEFFERSON CABRAL - ARACAJU",
    }

    df["NOME"] = df["NOME"].str.strip().replace(dict_names)

    return df


def main():
    df = get_complete_dataframe()
    df = fix_date(df)

    df = fix_names(df)

    df.to_csv("folha_completa_agosto_limpa.csv", index=False)

    df_names = df["NOME"].sort_values(ascending=True).drop_duplicates()
    df_names.to_csv("nomes_agosto_limpo.csv", index=False)


main()
