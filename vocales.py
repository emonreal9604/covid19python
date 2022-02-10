letra = input("Ingrese un letra\n").lower()  #.lower convierte a minuscula las letras
#letra=letra.lower esto es lo mismo
#.upper es para convertir a mayuscula
if letra=='a'or letra=='e'or letra=='i'or letra=='o'or letra=='u':
    print("La letra es una vocal")
else:
    print("La letra es una consonante")