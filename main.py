from src.selic import extrair_selic
from src.acoes import extrair_acoes
from src.processamento import combinar_dados, calcular_acumulado
from src.visualizacao import plot_acumulado, plot_correlacao
from src.indicadores import calcular_volatilidade, calcular_cagr, calcular_sharpe
from src.correlacao_dinamica import calcular_correlacao_dinamica, plotar_correlacao_dinamica
from src.cluster import clusterizar_ativos

import pandas as pd
import os
os.makedirs('figuras', exist_ok=True)


# Parâmetros
codigo_selic = 4390
inicio = '01/01/2010'
fim = '31/12/2023'
lista_acoes = ['ITUB4', 'EMBR3', 'VALE3']

# 1. Extração de dados
selic = extrair_selic(codigo_selic, inicio, fim)
acoes = extrair_acoes(lista_acoes, '2010-01-01', '2023-12-31')

# 2. Junta os dados e exibe a versão com NaNs (imagem 5/9)
dados = selic.copy()
for nome, serie in acoes.items():
    dados[nome] = serie
print(">>> DataFrame com retornos mensais (com NaN):")
print(dados.head(10))
print(f"{dados.shape[0]} rows × {dados.shape[1]} columns\n")

# 3. Remove primeira linha e soma 1 (imagem 4/9)
dados = dados.iloc[1:]
dados = dados + 1
print(">>> DataFrame após remover a primeira linha e somar 1:")
print(dados.head())

# 4. Cálculo acumulado e plot
acumulado = calcular_acumulado(dados)
plot_acumulado(acumulado)  # Imagem: gráfico “Ações vs Selic”
plot_correlacao(acumulado) # Imagem: heatmap de correlação


# 5. Indicadores
retornos_mensais = dados - 1
volatilidade = calcular_volatilidade(retornos_mensais)
cagr = calcular_cagr(acumulado)
selic_media = retornos_mensais['SELIC'].mean() * 12  # aproximação da taxa anual
sharpe = calcular_sharpe(cagr, volatilidade, selic_media)

# --- Correlação dinâmica (12 meses) ---
correlacoes_moveis = calcular_correlacao_dinamica(retornos_mensais, base_col='SELIC', janela=12)
plotar_correlacao_dinamica(correlacoes_moveis, janela=12)

# --- Clusterização por risco-retorno ---
clusterizar_ativos(cagr, volatilidade, n_clusters=3)

# Exibe tabela final
tabela_indicadores = pd.DataFrame({
    'Volatilidade (Anual)': volatilidade,
    'CAGR': cagr,
    'Sharpe Ratio': sharpe
})
print("\n📈 Indicadores Financeiros:\n")
print(tabela_indicadores.round(4))





