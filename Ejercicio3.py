'''
Un programa con 2 listas, que cree más listas

    Datos que aparecen en las dos listas
    Datos que en l1 si, y en l2, no
    Datos que aparecen en ambas listas
'''

l1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
l2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

#Eliminar elementos repetidos

a = set(l1)
b = set(l2)

union = list(a | b)
soloA = list(a - b)
interseccion = list(a & b)

print(f"Los datos que aparecen en las dos listas son: \n {union}")
print(f"Los datos que están en L1, pero no en L2 son: \n {soloA}")
print(f"Los datos que están en ambas listas son: \n {interseccion}")
