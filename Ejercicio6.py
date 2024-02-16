'''
Escribir un programa que pregunte al usuario por las ventas de un rango de años 
y muestre por pantalla un diagrama de líneas con la evolución de las ventas.
'''

#Importart libreria
import matplotlib.pyplot as plt

# Preguntamos por el año inicial
inicio = int(input('Introduce el año inicial: '))

# Preguntamos por el año final
fin = int(input('Introduce el año final: '))

# Definimos un diccionario vacío para guardar las ventas de cada año
ventas = {}

# Bucle iterativo para preguntar las ventas de cada año y guardarlas en el diccionario
# i toma como valores los años desde el año de inicio hasta el año final
for i in range(inicio, fin+1):
    # Preguntamos por las ventas del año i y las guardamos en el diccionario con la clave el año y el valor las ventas
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))


# Definimos la figura y los ejes del gráfico con Matplotlib
fig, ax = plt.subplots()
# Dibujamos la línea con las ventas a partir del diccionario
ax.plot(ventas.keys(), ventas.values())
# Mostarmos el gráfico por pantalla
plt.show()
