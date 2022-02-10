#Diccionarios Parte 2

equipo = {4:"Sergio Ramos",10:"Luka Modric",8:"Toni kroos",28:"Vinicius Júnior"}

print(equipo)
print(equipo.get(6,"No Existe jugador con ese dorsal")) #validar que un dato exista en el diccionario
print(1 in equipo) #Buscando un elemento en el diccionario
print(equipo.keys()) #mostrando solo las claves del diccionario
print(equipo.values())#mostrando solo los valores del diccionario
equipo.clear() #eliminando todos los elementos del diccionario

