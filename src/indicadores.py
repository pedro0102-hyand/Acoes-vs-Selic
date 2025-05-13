import pandas as pd
import numpy as np

def calcular_volatilidade(retornos: pd.DataFrame) -> pd.Series:
    return retornos.std() * np.sqrt(12)  # Volatilidade anualizada

def calcular_cagr(acumulado: pd.DataFrame) -> pd.Series:
    n_meses = acumulado.shape[0]
    anos = n_meses / 12
    return (acumulado.iloc[-1] / acumulado.iloc[0])**(1 / anos) - 1

def calcular_sharpe(cagr: pd.Series, volatilidade: pd.Series, taxa_livre: float) -> pd.Series:
    excesso_retorno = cagr - taxa_livre
    return excesso_retorno / volatilidade

