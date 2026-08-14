import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


def get_spreadsheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file("cedar-lexicon.json", scopes=scopes)
    client = gspread.authorize(creds)

    spreadsheet = client.open(title="interjornada", folder_id="1jV01RSXhwUTQ90u38ZXwep7KFAyWCQpv")

    return spreadsheet


def get_sheet(spreadsheet, title):
    return spreadsheet.worksheet(title)


def get_dataframe_agosto():

    spreadsheet = get_spreadsheet()
    sheet = get_sheet(spreadsheet, "JULHO - 2026")

    values = sheet.get("O1:W")

    headers = values[0]
    data = values[1:]

    df = pd.DataFrame(data, columns=headers)

    df.drop(df.columns[[2, 6]], axis=1, inplace=True)

    return df

def main():

    df = get_dataframe_agosto()

    df.to_csv("programacao_agosto_bruta.csv", index=False)

main()