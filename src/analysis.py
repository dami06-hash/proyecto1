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

    ruta_conclusiones = os.path.join('outputs', 'resultados', 'conclusiones.txt')
    
    with open(ruta_conclusiones, 'w', encoding='utf-8') as f:
        f.write("RESPUESTAS A LAS PREGUNTAS")
        f.write("1. ¿Cuál de las tres áreas tiene el promedio más alto?")
        f.write("Lectura (reading score) tiene el promedio más alto con 69.17 pts, seguida de escritura (68.05 pts) y matemáticas (66.09 pts).")
        
        f.write("2. ¿Los estudiantes que realizaron el curso de preparación presentan mejores resultados?")
        f.write("Sí. Quienes completaron el curso obtuvieron un promedio general de 72.67 pts, en comparación con 65.04 pts de quienes no lo realizaron.")
        
        f.write("3. ¿Existen diferencias en el rendimiento según el nivel educativo de los padres?")
        f.write("Sí. Se observa una relación directa: a mayor grado académico de los padres, mayor es el desempeño del estudiante.")
        
        f.write("4. ¿Qué porcentaje de estudiantes alcanza determinado promedio?")
        f.write("Rendimiento Medio (60 - 79 pts): 51.7%")
        f.write("Rendimiento Bajo (< 60 pts): 28.5%")
        f.write("Rendimiento Alto (> 80 pts): 19.8%")
        
        f.write("5. ¿Qué grupos presentan los promedios más altos y más bajos?")
        f.write("Por Etnia: El Grupo E presenta el promedio más alto (72.75 pts) y el Grupo A el más bajo (62.99 pts).")
        f.write("Por Tipo de Almuerzo: El grupo con Almuerzo Estándar obtiene el promedio más alto (70.84 pts), mientras que el grupo con Almuerzo Gratuito/Reducido registra el más bajo (62.20 pts).")
        
        f.write("CONCLUSIONES")
        f.write("El rendimiento académico de los estudiantes está fuertemente impulsado por factores" \
        " de apoyo y condiciones socioeconómicas: la preparación previa mediante cursos y un mayor nivel" \
        " educativo parental (o almuerzo estándar) elevan significativamente los promedios. " \
        "Por otro lado, matemáticas destaca como la materia con mayor rezago general, " \
        "marcando el área principal donde se deben concentrar los esfuerzos de reforzamiento.")

print("Lo que mas me costo a la hora de hacer este trabajo fue el clonar el url de mi compañero por que no me dejaba" \
"pero despues de estarlo intentanto varias veces pudimos clonarlo")