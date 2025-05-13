import pandas as pd

def extrair_selic(codigo: int, inicio: str, fim: str) -> pd.DataFrame:
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial={inicio}&dataFinal={fim}'
    df = pd.read_json(url)
    df.set_index('data', inplace=True)
    df.index = pd.to_datetime(df.index, dayfirst=True)
    df.columns = ['SELIC']
    df['SELIC'] = df['SELIC'] / 100
    return df
