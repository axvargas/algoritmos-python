'''
Created Date: Saturday September 11th 2021 11:24:18 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday September 11th 2021 11:33:07 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("graficado_simple.html")
    fig = figure(title="Graficado Simple", x_axis_label='x', y_axis_label='y')
    total_values = int(input("Ingrese el número de valores: "))
    x_values = list(range(total_values))
    y_values=[]
    for i in range(total_values):
        y_values.append(int(input(f"Ingrese el valor de y para el valor {i}: ")))
    fig.line(x_values, y_values, legend_label="Linea 1", line_width=2)
    show(fig)