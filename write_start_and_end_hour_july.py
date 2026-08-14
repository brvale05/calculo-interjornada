import pandas as pd


def get_dataframe_programacao_julho_bruta():

    df = pd.read_csv("programacao_julho_bruta.csv")

    return df


def get_dataframe_folha_completa_limpa():

    df = pd.read_csv("folha_completa_limpa.csv")

    return df


def clean_data(df):

    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    return df


# LEFT JOIN
def fill_hours_df_prog_julho_bruta(df_left, df_right):
    # 1. Realiza o cruzamento (left join) entre B e as colunas de interesse de A
    # O left join garante que o dataframe B não perca nenhuma de suas linhas originais
    df_left = df_left.merge(
        df_right[['DIA', 'NOME', 'ENTRADA', 'SAÍDA']],
        left_on=['DATA', 'MOT. 1'],
        right_on=['DIA', 'NOME'],
        how='left'
    )

    # 2. Atualiza as colunas de B com os valores encontrados de A
    # O fillna garante que, se não houver correspondência, o valor original de B seja mantido
    df_left['HORA INÍCIO MOT. 1'] = df_left['ENTRADA'].fillna(df_left['HORA INÍCIO MOT. 1'])
    df_left['HORA FIM MOT. 1'] = df_left['SAÍDA'].fillna(df_left['HORA FIM MOT. 1'])

    # 3. Remove as colunas auxiliares trazidas do dataframe A para limpar a tabela
    df_left = df_left.drop(columns=['DIA', 'NOME', 'ENTRADA', 'SAÍDA'])

    return df_left


def main():

    df_prog_julho = get_dataframe_programacao_julho_bruta()
    df_folha_completa = get_dataframe_folha_completa_limpa()

    df_prog_julho = clean_data(df_prog_julho)
    df_folha_completa = clean_data(df_folha_completa)

    df_novo = fill_hours_df_prog_julho_bruta(df_prog_julho, df_folha_completa)

    df_novo.to_csv("start_and_end_hour_prog_julho.csv", index=False, columns=["HORA INÍCIO MOT. 1", "HORA FIM MOT. 1"])
    # df_novo.to_csv("start_and_end_hour_prog_julho.csv", index=False)

main()

