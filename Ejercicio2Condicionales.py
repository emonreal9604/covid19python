'''
Hacer un programa que pida 3 numeros y determine el mayor
'''
n1=int(input("Ingrese un numero\n"))
n2=int(input("Ingrese un numero\n"))
n3=int(input("Ingrese un numero\n"))
if n1>=n2 and n1>=n3:
    print(f"El numero mayor es {n1}")
if n2>=n1 and n2>=n3:
    print(f"El numero mayor es {n2}")
if n3>=n1 and n3>=n2:
    print(f"El numero mayor es {n3}")



