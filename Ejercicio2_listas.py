'''
Colecciones - Ejercicio 2:
Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas
'''
lista1 = [1,2,3,4,5,6,4,3,8,9]
lista2 = [7,8,9,9,2,3,1,0,11,2]
a = set(lista1)
b = set(lista2)
union =list( a | b)
soloA = list(a-b)
soloB = list(b-a)
interseccion = list(a & b)
print(union)
print(soloA)
print(soloB)
print(interseccion)