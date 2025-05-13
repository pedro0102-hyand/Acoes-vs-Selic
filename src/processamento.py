import pandas as pd

def combinar_dados(selic_df: pd.DataFrame, acoes_dict: dict) -> pd.DataFrame:
    df = selic_df.copy()
    for nome, serie in acoes_dict.items():
        df[nome] = serie
    df = df.iloc[1:]  # Remove a primeira linha com NaNs
    df += 1           # Soma 1 para cálculo do produto acumulado
    return df

def calcular_acumulado(df: pd.DataFrame) -> pd.DataFrame:
    return df.cumprod()
