opc=int(input("Elija una opción 1-Suma 2-Resta 3-Multiplicación 4-Divion\n"))

if opc==1:
    n1=float(input("Ingrese un numero"))
    n2 = float(input("Ingrese un numero"))
    total=n1+n2
    print(f"La suma es: {total:.2f}")
elif opc==2:
    n1=float(input("Ingrese un numero"))
    n2=float(input("Ingrese un numero"))
    total=n1-n2
    print(f"La resta es: {total:.2f}")
elif opc==3:
    n1=float(input("Ingrese un numero"))
    n2 = float(input("Ingrese un numero"))
    total=n1*n2
    print(f"La multiplicación es: {total:.2f}")
elif opc==4:
    n1=float(input("Ingrese un numero"))
    n2 =float(input("Ingrese un numero"))
    total=n1/n2
    print(f"La divion es: {total:.2f}")
elif opc>=5 or opc<=0:
    print("Opcion Invalida")


