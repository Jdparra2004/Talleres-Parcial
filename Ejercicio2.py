'''
Escribe un programa donde tenga una lista y que elimine los elemntos
repetidos, por último mostrar la lista
'''

#listas
numeros = [1,2, 1, 2, 3, 5,4, 6, 3, 5, 3, 7, 8, 9]
nombres = ["Alejandro", "Juan", "Aleja", "María", "Juan", "María", "Alejandro", "Sara"]
ciudades = ["Medellín", "Bogotá", "Cali", "Barranquilla", "Medellín", "Bogotá", "Cartagena"]

#lista general
lista = numeros+nombres+ciudades
print(f"La lista general es:\n {lista}")

#método 1
conjunto = set(lista)#con el conjunto podemos eliminar elementos repetidos
lista = list(conjunto)
print(f"la lista obtenida es:\n {lista}")

#método 2
lista1 = list(set(lista))#hacer lo anterior pero en una sola linea

print(f"la lista obtenida es:\n {lista}")
