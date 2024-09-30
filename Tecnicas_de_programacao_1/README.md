
# DataQuality - Análise de Qualidade de Dados

## Descrição

O **DataQuality** é um módulo para realizar análises automáticas e detalhadas de qualidade de dados em DataFrames utilizando bibliotecas populares do ecossistema Python, como **pandas**, **matplotlib**, **seaborn**, **ydata-profiling** e **SweetViz**. Este projeto facilita a detecção de valores nulos, outliers, análise de distribuição de variáveis e geração de relatórios automáticos, tornando a avaliação da qualidade de dados rápida e acessível.

## Funcionalidades

O módulo **DataQuality** oferece as seguintes funcionalidades:

1. **Análise de Valores Nulos**: Retorna a contagem de valores nulos para cada coluna do DataFrame.
2. **Análise de Valores Únicos**: Exibe a contagem de valores únicos por coluna.
3. **Análise de Colunas Categóricas**: Mostra a contagem de valores em colunas categóricas.
4. **Análise Numérica**: Exibe estatísticas descritivas para colunas numéricas, como média, mediana e desvio padrão.
5. **Distribuição de Variáveis Numéricas**: Plota gráficos de distribuição para variáveis numéricas.
6. **Distribuição de Variáveis Categóricas**: Plota gráficos de distribuição para variáveis categóricas.
7. **Detecção de Outliers**: Identifica outliers em colunas numéricas usando o intervalo interquartil (IQR).
8. **Matriz de Correlação**: Gera e exibe uma matriz de correlação para colunas numéricas.
9. **Relatórios Automáticos**:
   - **YData Profiling**: Gera um relatório exploratório automático e interativo do DataFrame.
   - **SweetViz**: Gera um relatório completo de visualização de dados em HTML.

## Instalação

Para usar este projeto, siga os seguintes passos:

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Certifique-se de que as bibliotecas necessárias estão instaladas:
   ```bash
   pip install pandas matplotlib seaborn ydata-profiling sweetviz
   ```

## Como Usar

1. Importe o módulo **DataQuality** e carregue seu dataset em um DataFrame do Pandas:

   ```python
   import pandas as pd
   from data_quality import DataQuality

   # Carregar seu dataset
   df = pd.read_csv('seu_dataset.csv')

   # Instanciar a classe DataQuality
   dq = DataQuality(df)
   ```

2. Utilize as funcionalidades conforme necessário:

   ```python
   # Exemplo: Geração de relatório completo
   dq.relatorio()
   ```

### Exemplos de Funcionalidades

- **Valores Nulos**:
   ```python
   print(dq.valores_nulos())
   ```

- **Distribuição Numérica**:
   ```python
   dq.plot_distribuicao_numerica()
   ```

- **Relatório com SweetViz**:
   ```python
   dq.sweetviz_report()
   ```

## Relatórios Automáticos

Este projeto também permite a criação de relatórios automáticos com visualizações interativas:

1. **YData Profiling**:
   Gera um relatório detalhado do DataFrame, com gráficos interativos, estatísticas descritivas e correlações.
   
   ```python
   dq.ydata_profiling_report()
   ```

2. **SweetViz**:
   Cria um arquivo HTML com visualizações automáticas.

   ```python
   dq.sweetviz_report()
   ```
