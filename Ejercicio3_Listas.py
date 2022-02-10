'''
Colecciones - Ejercicio 3:
Escriba un programa donde cree una lista con los siguientes personajes del Señor de los anillos.

Nombre: Aragorn
Clase: Guerrero
Raza: Dúnadan del Norte

Nombre: Gandalf
Clase: Mago
Raza: Istar

Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar
'''
personajes = []  #creando lista vacia
p1 = {"Nombre":"Aragorn","Clase":"Guerrero","Raza":"Dúnadan del Norte"}
p2 = {"Nombre":"Gandalf","Clase":"Mago","Raza":"Istar"}
p3 = {"Nombre":"Legolas","Clase":"Arquero","Raza":"Elfo Sindar"}
personajes.append(p1) #añadiendo personaje a la lista
personajes.append(p2) #añadiendo personaje a la lista
personajes.append(p3) #añadiendo personaje a la lista

print(personajes)