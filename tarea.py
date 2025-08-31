def encontrar_k(letras, K):
    vistos = set()  
    pares = []

    for x in letras:
        if (K - x) in vistos:
            pares.append((K - x, x))
        vistos.add(x)

    return pares

numero = int(input("¿Cuántos números quieres ingresar? "))
letras = []

for i in range(numero):
    letra = int(input(f"Ingrese el número {i+1}: "))
    letras.append(letra)

K = int(input("Ingresa el valor de K: "))

resultado = encontrar_k(letras, K)

if resultado:
    print("Pares que suman K:")
    for par in resultado:
        print(par)
else:
    print("No hay pares que sumen K.")