import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv
import matplotlib.pyplot as plt
import seaborn as sns

class DataQuality:
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def valores_nulos(self):
        return self.df.isnull().sum()
    
    def valores_unicos(self):
        return self.df.nunique()
    
    def valores_colunas(self, coluna):
        if coluna in self.df.select_dtypes(include=['object', 'category']).columns:
            return self.df[coluna].value_counts()
        else:
            raise ValueError(f"Coluna '{coluna}' não é categórica.")
    
    def descricao_numerica(self):
        return self.df.describe()
    
    def descricao_categorica(self):
        return self.df.describe(include=['object', 'category'])

    def plot_distribuicao_numerica(self):
        num_cols = self.df.select_dtypes(include=['number']).columns
        
        if num_cols.empty:
            print("Nenhuma coluna numérica encontrada.")
            return
        
        for col in num_cols:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.df[col], kde=True, bins=40, color='green')
            plt.title(f"Distribuição de {col}", fontsize=14)
            plt.xlabel(col, fontsize=12)
            plt.ylabel("Frequência", fontsize=12)
            plt.tight_layout()
            plt.show()

    def plot_distribuicao_categorica(self):
        cat_cols = self.df.select_dtypes(include=['object', 'category']).columns
        
        if cat_cols.empty:
            print("Nenhuma coluna categórica encontrada.")
            return
        
        for col in cat_cols:
            unique_vals = self.df[col].nunique()

            plt.figure(figsize=(10, 6))
            sns.countplot(x=self.df[col], order=self.df[col].value_counts().index, hue=self.df[col], palette="pastel", legend=False)
            plt.title(f"Distribuição de {col}")
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()

    def detect_outliers(self):
        outliers = {}
        num_cols = self.df.select_dtypes(include=['number']).columns
        for col in num_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers_in_col = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
            outliers[col] = outliers_in_col
        return outliers

    def matriz_correlacao(self):
        num_cols = self.df.select_dtypes(include=['number'])
    
        if num_cols.empty:
            print("Nenhuma coluna numérica encontrada para calcular a matriz de correlação.")
            return None

        corr_matrix = num_cols.corr()
        plt.figure(figsize=(10, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='plasma', linewidths=0.5) 
        plt.title("Matriz de Correlação")
        plt.show()
        return corr_matrix


    def ydata_profiling_report(self):
        profile = ProfileReport(self.df, title="YData Profiling Report", explorative=True)
        profile.to_notebook_iframe()
    
    def sweetviz_report(self):
        report = sv.analyze(self.df)
        report.show_html("sweetviz_report.html")
        print("Relatório SweetViz salvo como sweetviz_report.html")
    
    def relatorio(self):
        print("Valores Nulos:")
        print(self.valores_nulos())
        print("\nValores Únicos:")
        print(self.valores_unicos())
        print("\nDescrição Numérica:")
        print(self.descricao_numerica())
        print("\nDescrição Categórica:")
        print(self.descricao_categorica())
        print("\nDetectando Outliers:")
        outliers = self.detect_outliers()
        for col, data in outliers.items():
            print(f"\nOutliers em {col}:")
            print(data)
        print("\nPlotando Distribuições Numéricas:")
        self.plot_distribuicao_numerica()
        print("\nPlotando Distribuições Categóricas:")
        self.plot_distribuicao_categorica()
        print("\nMatriz de Correlação:")
        self.matriz_correlacao()
        print("\nGerando Relatório: YData Profiling...")
        self.ydata_profiling_report()
        print("\nGerando Relatório: SweetViz...")
        self.sweetviz_report()

