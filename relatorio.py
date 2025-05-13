import pandas as pd
import os
from datetime import datetime
from src.indicadores import calcular_volatilidade, calcular_cagr, calcular_sharpe
from src.processamento import calcular_acumulado
from src.acoes import extrair_acoes
from src.selic import extrair_selic

# --- Parâmetros
codigo_selic = 4390
inicio = '01/01/2010'
fim = '31/12/2023'
lista_acoes = ['ITUB4', 'EMBR3', 'VALE3']

# --- Extração e processamento
selic = extrair_selic(codigo_selic, inicio, fim)
acoes = extrair_acoes(lista_acoes, '2010-01-01', '2023-12-31')

dados = selic.copy()
for nome, serie in acoes.items():
    dados[nome] = serie

dados = dados.iloc[1:]
dados += 1
acumulado = calcular_acumulado(dados)
retornos_mensais = dados - 1

# --- Indicadores
volatilidade = calcular_volatilidade(retornos_mensais)
cagr = calcular_cagr(acumulado)
selic_media = retornos_mensais['SELIC'].mean() * 12
sharpe = calcular_sharpe(cagr, volatilidade, selic_media)

# --- Tabela final
tabela = pd.DataFrame({
    'Volatilidade (Anual)': volatilidade,
    'CAGR': cagr,
    'Sharpe Ratio': sharpe
}).round(4)

# --- Geração do arquivo TXT
os.makedirs("relatorio", exist_ok=True)
agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open('relatorio/analise_estatistica.txt', 'w') as f:
    f.write(f"Relatório de Análise Estatística - {agora}\n")
    f.write("="*60 + "\n")
    f.write("\n▶️ Indicadores Financeiros:\n\n")
    f.write(tabela.to_string())
    f.write("\n\n▶️ Matriz de Correlação Estática:\n\n")
    f.write(acumulado.corr().round(2).to_string())
    f.write("\n\n✅ Fim do relatório.")
