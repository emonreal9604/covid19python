'''
Colecciones - Ejercicio 1:
Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos, por último mostrar la lista
'''
lista = [1,2,3,1,2,"Eleazar",4,2,5]
print(lista)
conjunto = set(lista) #convirtiendo la lista a un conjuto
lista=list(conjunto) #regresando el conjunto a lista con el metodo list()
#otra manera de hacerlo más facíl
#lista = list(set(lista))
print(lista)