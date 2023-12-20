import pandas as pd
import plotly.express as px

# Dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Boxplot de distribución de notas con Plotly
fig_boxplot = px.box(df, x='materia', y='nota', title='Distribución de Notas por Materia', points='all')
fig_boxplot.update_layout(xaxis_title='Materias', yaxis_title='Notas')
fig_boxplot.show()

# Pie chart de distribución de aprobados con Plotly
aprobados_counts = df['aprobado'].value_counts()
fig_piechart = px.pie(aprobados_counts, names=aprobados_counts.index, title='Proporción de Estudiantes Aprobados y No Aprobados')
fig_piechart.show()
