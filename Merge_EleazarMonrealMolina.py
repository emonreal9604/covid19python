def merge(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2  #divide el el arreglo a la mitad
        L = lista[:mitad]  # subarreglo izquierdo
        R = lista[mitad:]  # subarreglo derecho

        merge(L)  #llamando la funcion para subarreglo derecho
        merge(R)  # llamando la funcion para subarreglo derecho
        i = j = k = 0

        # copiando a los arreglos temporales L[] and R[]
        while i < len(L) and j < len(R): #mientras no se salga del tamaño del arreglo
            if L[i] < R[j]: #determina el elemento que sigue en el orden
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

# Funcion para imprimir el arreglo
def imprimir(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()

if __name__ == '__main__':
    lista = [10,9,7,5,4,3,1,2,6,-890]
    print("Arreglo desordenado:", end="\n")
    imprimir(lista)#llamando a la función imprimir
    merge(lista) #llamando a la funcion merge
    print(f"Arreglo Ordenado: ", end="\n")
    imprimir(lista)#llamando a la función imprimir
