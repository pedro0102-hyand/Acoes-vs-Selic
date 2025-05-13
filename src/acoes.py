import yfinance as yf
import pandas as pd

def extrair_acoes(lista_acoes: list, inicio: str, fim: str) -> dict:
    dados = {}
    for ativo in lista_acoes:
        ticker = ativo + '.SA'
        print(f"📥 Baixando dados de {ticker}...")
        df = yf.download(
            ticker,
            start=inicio,
            end=fim,
            interval='1mo',
            auto_adjust=False,
            progress=False
        )

        if 'Adj Close' in df.columns:
            dados[ativo] = df['Adj Close'].pct_change()
        else:
            print(f"⚠️ Coluna 'Adj Close' não encontrada para {ativo}, pulando...")
    
    return dados

