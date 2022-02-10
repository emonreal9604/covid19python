#Tuplas
#En las tuplas no se pueden modificar los elementos que se ingresan al inicio
tupla = (1,4.5664,"hola",True,[1,2,3])
print(1 in tupla)
print(tupla.index("hola"))
print(tupla.count(1))
print(len(tupla))
lista = list(tupla) #convertir una tupla a una lista
print(lista)
lista1 = [1,2,4,"Mundo"]
tupla1 = tuple(lista1) #convirtiendo una lista a una tupla
print(tupla1)