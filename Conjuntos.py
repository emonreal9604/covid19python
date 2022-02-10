#Conjuntos
#Son grupos de elementos desordenados donde no se pueden repetir los elementos

conjunto = set()
conjunto = {1,2,3,"Eleazar",False,3.455}

conjunto.add(6) #agregando elementos a un conjunto
conjunto.add("Adios")
conjunto.add('s')
conjunto.discard(1) #eliminando elementos de un conjunto
#conjunto.clear() #eliminando todos los elementos del conjunto
print(conjunto)

a = {1,2,3}
b = {3,4,5,6}
c = a|b #union de 2 conjuntos
d = a&b #interseccion de 2 conjunto
e = a - b #elementos que estan en A y no en B
f = b - a #elementos que estan en B y no en A
g = a ^ b #Diferencia simetrica
print(f"a U b = {c}")
print(f"Interseccion A , B = {d}")
print(f"A - B = {e}")
print(f"B - A = {f}")
print(f"Diferencia simetrica A,B = {g}")
# saber si a o b son subconjuntos del conjunto H
h = {1,2,3,4,5,6,7}
print(a.issubset(h)) # A es subconjunto de H
print(b.issubset(h)) # B es subconjunto de H
print(a.issuperset(h)) # A no es superconjunto de H
print(b.issuperset(h)) # B no es superconjunto de H
print(a.isdisjoint(b)) #A no tiene ningun elemento de B
#frozen.set() sirve para hacer un conjunto inmutable
#a = frozenset(1,2,3)