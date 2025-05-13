import pandas as pd
import matplotlib.pyplot as plt
import os

def calcular_correlacao_dinamica(df: pd.DataFrame, base_col: str = 'SELIC', janela: int = 12) -> dict:
    correlacoes = {}
    for col in df.columns:
        if col != base_col:
            correlacoes[col] = df[base_col].rolling(janela).corr(df[col])
    return correlacoes

def plotar_correlacao_dinamica(correlacoes: dict, janela: int):
    os.makedirs('figuras', exist_ok=True)
    for ativo, serie in correlacoes.items():
        if serie.isnull().all():
            print(f"⚠️ Nenhuma correlação válida para {ativo}")
            continue
        plt.figure(figsize=(10, 5))
        plt.title(f'Correlação Móvel ({janela} meses) - {ativo} vs SELIC')
        plt.plot(serie.index, serie, label=f'{ativo} x SELIC')
        plt.axhline(0, color='black', linestyle='--', linewidth=1)
        plt.ylabel('Correlação')
        plt.xlabel('Tempo')
        plt.legend()
        plt.tight_layout()
        path = f'figuras/correlacao_dinamica_{ativo}.png'
        plt.savefig(path)
        plt.close()
        print(f"✅ Gráfico salvo: {path}")
