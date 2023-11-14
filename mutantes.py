print("--------------------------------------------")
print("Comienzo del programa mutantes.....")
print("--------------------------------------------")

print("Ingrese las filas de la matriz de ADN:")
print("Las letras validas son: A, T, C, G.")

dna = []
for i in range(6):
    fila = input(f"Fila nro {i + 1}: ").upper()
    while len(fila) != 6 or any(letra not in "ATCG" for letra in fila):
        print("Recuerde ingresar exactamente 6 letras válidas (A, T, C, G).")
        fila = input(f"Fila nro {i + 1}: ").upper()
    print("Fila agregada correctamente.")
    dna.append(fila)

print("--------------------------------------------")
print("Matriz de ADN ingresada:")
print("--------------------------------------------")
for fila in dna:
    print("\t".join(fila))
print("--------------------------------------------")


def isMutant(dna):
    secuencias_encontradas = 0

    for fila in dna: # verifico las horizontales
        for i in range(len(fila) - 3):
            if len(set(fila[i:i+4])) == 1:
                secuencias_encontradas += 1
                if secuencias_encontradas >= 2:
                    return True

    for columna in range(len(dna[0])): # verifico las verticales
        for i in range(len(dna) - 3):
            if len(set(dna[fila][columna] for fila in range(i, i+4))) == 1:
                secuencias_encontradas += 1
                if secuencias_encontradas >= 2:
                    return True

    for i in range(len(dna) - 3):  #verifico las diagonales
        for j in range(len(dna[0]) - 3):
            if len(set(dna[i+k][j+k] for k in range(4))) == 1:
                secuencias_encontradas += 1
                if secuencias_encontradas >= 2:
                    return True
            if len(set(dna[i+k][j+3-k] for k in range(4))) == 1:
                secuencias_encontradas += 1
                if secuencias_encontradas >= 2:
                    return True

    return secuencias_encontradas >= 2


if isMutant(dna):
    print("El ADN es mutante.")
else:
    print("El ADN no es mutante.")
print("--------------------------------------------")
