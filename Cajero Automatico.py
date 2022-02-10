print("\tMenu")
print("1-Ingresar Dinero a la Cuenta")
print("2-Retirar Dinero de la Cuenta")
print("3-Mostrar Dinero Disponible")
print("4-Salir")
opc=int(input("!Seleccione un Opción Valida¡\n"))
saldo=1000
print()
if opc==1:
    print(f"Saldo Inicial: {saldo:.2f}")
    aux=float(input("¿Cuanto dinero desea ingresar a la cuenta?\n"))
    saldo+=aux
    print(f"Saldo Actual: {saldo:.2f}")
elif opc==2:
    retirar=float(input("¿Cuanto dinero desea retirar?\n"))
    if retirar>saldo:
        print("NO puede retirar esa cantidad ya que es mayor al saldo actual\n")
    else:
        saldo -= retirar
        print(f"Saldo restante: {saldo:.2f}\n")
elif opc==3:
    print(f"Saldo Actual: {saldo:.2f}\n")
elif opc==4:
    print("Gracías por Utilizar su Cajero Automatico")
else:
    print("Opcion Invalida Pruebe de Nuevo")

