# 📈 Análise Financeira: Ações vs SELIC (2010–2023)

Este projeto realiza uma análise comparativa entre o desempenho de ações brasileiras e a taxa SELIC no período de 2010 a 2023. Utilizando ferramentas de **ciência de dados**, **estatística financeira** e **visualização gráfica**, o sistema gera relatórios automáticos em formato `.txt` e `.pdf`, além de gráficos interpretativos.

---

## 🔧 Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas** – manipulação de dados
- **Matplotlib** – visualizações
- **ReportLab** – geração de PDFs
- **scikit-learn** – clusterização
- **yfinance** – extração de cotações de ações
- **SELIC API/Bacen** – extração da taxa básica de juros
---

## 📂 Estrutura do Projeto

```
├── main.py                         # Pipeline principal de análise
├── relatorio.py                   # Geração de relatório em TXT
├── pdf.py                         # Geração de relatório em PDF
├── figuras/                       # Gráficos gerados automaticamente
├── relatorio/
│   ├── analise_estatistica.txt    # Relatório em texto (indicadores e correlação)
│   └── analise_final.pdf          # Relatório visual em PDF
└── src/
    ├── selic.py                   # Função de extração da SELIC
    ├── acoes.py                   # Função de extração de ações (via yfinance)
    ├── processamento.py           # Combinação de dados e cálculo acumulado
    ├── visualizacao.py           # Funções de visualização e gráficos
    ├── indicadores.py            # Cálculo de volatilidade, CAGR, Sharpe
    ├── correlacao_dinamica.py    # Correlação móvel de 12 meses
    └── cluster.py                # Agrupamento de ativos por risco-retorno
```

---

## 📊 Indicadores Calculados

- **Volatilidade Anualizada**
- **CAGR (Crescimento Anual Composto)**
- **Sharpe Ratio (ajustado pela SELIC média anual)**

---

## 📌 Como Executar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute a análise principal:
```bash
python main.py
```

3. Gere os relatórios:
```bash
python relatorio.py
python pdf.py
```

---

## 🧠 Resultados e Interpretação

- Gráficos comparativos entre **ações e SELIC**
- **Heatmap de correlação estática**
- **Correlação móvel (janela de 12 meses)**
- **Clusterização** dos ativos em função do risco-retorno
- Relatórios salvos automaticamente nas pastas `relatorio/` e `figuras/`

---

## 📁 Exemplo de Saída

### `relatorio/analise_estatistica.txt`
```
Volatilidade (Anual)    CAGR  Sharpe Ratio
SELIC                0.0097  0.0928        0.3345
ITUB4                0.2948  0.0739       -0.0530
...
```

### `relatorio/analise_final.pdf`

> Contém gráficos:
> - Retorno acumulado
> - Correlação
> - Cluster de risco-retorno
> - Correlação dinâmica por ativo

