#Listas_Colecciones

lista = [1,2,4,5,"Hola Mundo",2,3,4,2,1,3]
#añadiendo elementos a la lista al final
lista.append(6)
lista.append("Eleazar")
#insertando un elemento en una posicion especifica
lista.insert(2,3)
lista.insert(0,0)
#Añadiendo varios elementos a la lista
lista.extend([7,8,9,10])
print(lista)
#sumando dos listas
lista1 =[1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3= lista1+lista2
print(lista3)
#saber si un elemento esta en la lista
print(2 in lista)
#buscar un elemento en la lista, con su posicion
print("El elemento esta en la posicion: ",lista.index("Eleazar"))
#Saber cuantas veces aparece un elemento en la lista
print(lista.count(3)) #En este caso cuantas veces aparece el numero 3 en la lista

#Poner la lista al reves
lista.reverse()
print(lista)
#multiplicando una lista
lista4 = [11,12,13,14,15]*2
print(lista4)
#Ordenar elementos de una lista
lista5=[-2,3,0,1]
lista5.sort() #Ordenando ascendentemente
lista5.sort(reverse=True) #ordenando descendentemente
print(lista5)

#Como eliminar dato de una lista
lista.pop(1)#Eliminando el elemento de la poscion 1 de la lista
print(lista)
#Eliminando un elemento de la lista sin saber su posicion
lista.remove("Eleazar")
print(lista)
#Eliminando todos los elementos de la lista
lista.clear()
print(lista)
#Poner la lista al reves
lista.reverse()
print(lista)
