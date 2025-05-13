import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

def clusterizar_ativos(cagr: pd.Series, volatilidade: pd.Series, n_clusters=3):
    os.makedirs('figuras', exist_ok=True)

    # Monta o DataFrame com as features
    df = pd.DataFrame({
        'CAGR': cagr,
        'Volatilidade': volatilidade
    }).dropna()

    modelo = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = modelo.fit_predict(df[['CAGR', 'Volatilidade']])

    # Visualização
    plt.figure(figsize=(8, 6))
    cores = ['red', 'green', 'blue', 'orange', 'purple']
    for i in range(n_clusters):
        cluster_data = df[df['Cluster'] == i]
        plt.scatter(cluster_data['Volatilidade'], cluster_data['CAGR'],
                    color=cores[i % len(cores)], label=f'Grupo {i}', s=100)

    for nome, linha in df.iterrows():
        plt.text(linha['Volatilidade'] + 0.002, linha['CAGR'], nome)

    plt.xlabel('Volatilidade Anual')
    plt.ylabel('CAGR')
    plt.title('Clusterização de Ativos por Risco-Retorno')
    plt.legend()
    plt.tight_layout()
    path = 'figuras/cluster_risco_retorno.png'
    plt.savefig(path)
    plt.close()
    print(f"📊 Cluster plot salvo: {path}")

