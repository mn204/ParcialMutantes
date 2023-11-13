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
for fila in dna:
    print(" ".join(fila))
print("--------------------------------------------")


