import time

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


def get_spreadsheet_junho():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file("cedar-lexicon.json", scopes=scopes)
    client = gspread.authorize(creds)

    spreadsheet = client.open(title="FOLHA JUNHO", folder_id="1jV01RSXhwUTQ90u38ZXwep7KFAyWCQpv")

    return spreadsheet


def get_spreadsheet_julho():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file("cedar-lexicon.json", scopes=scopes)
    client = gspread.authorize(creds)

    spreadsheet = client.open(title="FOLHA JULHO", folder_id="1jV01RSXhwUTQ90u38ZXwep7KFAyWCQpv")

    return spreadsheet



def get_dataframe_junho():
    spreadsheet = get_spreadsheet_junho()

    dados_completos = []

    for sheet in spreadsheet.worksheets():
        title = sheet.title.upper()
        values = sheet.get("B15:F46")

        headers = values[0]
        data = values[17:]

        data_fixed = []
        for row in data:
            # Se a linha veio menor que o cabeçalho, adiciona itens vazios ('') no final
            if len(row) < len(headers):
                row.extend([''] * (len(headers) - len(row)))

            # O [:len(headers)] garante que a linha não terá mais elementos que o cabeçalho
            data_fixed.append(row[:len(headers)])

        # Cria o dataframe com a lista corrigida
        df = pd.DataFrame(data_fixed, columns=headers)

        df['NOME'] = title
        df['MES'] = 'JUNHO'

        df.drop(df.columns[[2, 3]], axis=1, inplace=True)

        dados_completos.append(df)

        time.sleep(3)

    if dados_completos:
        return pd.concat(dados_completos, ignore_index=True)
    else:
        return pd.DataFrame()

def get_dataframe_julho():
    spreadsheet = get_spreadsheet_julho()

    dados_completos = []

    for sheet in spreadsheet.worksheets():
        title = sheet.title.upper()
        values = sheet.get("B13:F43")

        headers = values[0]
        data = values[1:]

        data_fixed = []
        for row in data:
            # Se a linha veio menor que o cabeçalho, adiciona itens vazios ('') no final
            if len(row) < len(headers):
                row.extend([''] * (len(headers) - len(row)))

            # O [:len(headers)] garante que a linha não terá mais elementos que o cabeçalho
            data_fixed.append(row[:len(headers)])

        # Cria o dataframe com a lista corrigida
        df = pd.DataFrame(data_fixed, columns=headers)

        df['NOME'] = title
        df['MES'] = 'JULHO'

        df.drop(df.columns[[2, 3]], axis=1, inplace=True)

        dados_completos.append(df)

        print(df)

        time.sleep(3)

    if dados_completos:
        return pd.concat(dados_completos, ignore_index=True)
    else:
        return pd.DataFrame()