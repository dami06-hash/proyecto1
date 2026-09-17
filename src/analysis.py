import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

   # 1. Se cargo el dataset
    data_path = os.path.join('data', 'dataset.csv')
    if not os.path.exists(data_path):
        data_path = os.path.join('data', 'data.csv')

    df = pd.read_csv(data_path)
    
    # 3. Informacion del dataset
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


    # 3. Limpieza y preprocesamiento
    df = df.drop_duplicates()


    # 4. Crear columna de promedio general
    score_cols = ['math score', 'reading score', 'writing score']
    df['average_score'] = df[score_cols].mean(axis=1)


    # 5. Clasificar rendimiento
    def clasificar_rendimiento(score):
        if score < 60:
            return 'Bajo'
        elif score < 80:
            return 'Medio'
        else:
            return 'Alto'

    df['rendimiento_categoria'] = df['average_score'].apply(clasificar_rendimiento)

    
    os.makedirs(os.path.join('outputs', 'resultados'), exist_ok=True)


    # 6. Analisis de los datos 
    print("PROMEDIO POR MATERIA")
    print(df[score_cols].mean())

    print("PROMEDIO POR CURSO DE PREPARACION")
    print(df.groupby('test preparation course')['average_score'].mean())

    print("PROMEDIO POR NIVEL EDUCATIVO DE PADRES")
    print(df.groupby('parental level of education')['average_score'].mean())

    print("PORCENTAJE POR CATEGORIA DE RENDIMIENTO")
    print(df['rendimiento_categoria'].value_counts(normalize=True) * 100)


        # Gráfico 1: Promedio por materia
    plt.figure()
    sns.barplot(x=score_cols, y=df[score_cols].mean().values)
    plt.title('Promedio por Materia')
    plt.savefig('outputs/resultados/promedio_por_materia.png')
    plt.close()

    # Gráfico 2: Rendimiento vs Curso de preparación
    plt.figure()
    sns.boxplot(x='test preparation course', y='average_score', data=df)
    plt.title('Promedio vs Curso de Preparacion')
    plt.savefig('outputs/resultados/curso_preparacion_vs_promedio.png')
    plt.close()

    # Gráfico 3: Distribución por categorías
    plt.figure()
    sns.countplot(x='rendimiento_categoria', data=df, order=['Bajo', 'Medio', 'Alto'])
    plt.title('Distribucion de Rendimiento')
    plt.savefig('outputs/resultados/distribucion_rendimiento.png')
    plt.close()

if __name__ == '__main__':
    main()


