
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_acumulado(df: pd.DataFrame, path='figuras/acoes_vs_selic.png'):
    os.makedirs('figuras', exist_ok=True)
    plt.figure(figsize=(10, 6))
    sns.set_style('darkgrid')
    sns.set_palette('mako')
    plt.title('Ações vs Selic')
    sns.lineplot(data=df)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    print(f"✅ Gráfico salvo em: {path}")

def plot_correlacao(df: pd.DataFrame, path='figuras/correlacao_retorno.png'):
    os.makedirs('figuras', exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.title('Correlação do Retorno Acumulado')
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, vmin=-1, vmax=1)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    print(f"✅ Gráfico salvo em: {path}")

