import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
   
    data_path = os.path.join('data', 'dataset.csv')
    if not os.path.exists(data_path):
        data_path = os.path.join('data', 'dtset.csv')

    df = pd.read_csv(data_path)
    
    
    print("INFORMACION DEL DATASET")
    df.info()

    print("PRIMEROS REGISTROS")
    print(df.head())

    print("ESTADISTICAS")
    print(df.describe())

    print("VALORES NULOS")
    print(df.isnull().sum())

    print("REGISTROS DUPLICADOS")
    print(df.duplicated().sum())