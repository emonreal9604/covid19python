'''Realizar un programa que lea 2 nums y diga cual es par o si son ambos'''
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un numero: "))

if x%2==0 and y%2==0:
    print("Ambos numeros son pares")
elif (x%2==0) and y%2!=0:
    print(f"El numero {x} es par")
elif y%2==0and x%2!=0:
    print(f"El numero {y} es par")
else:
    print("Ambos numeros son impares")