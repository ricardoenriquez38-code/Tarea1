def encontrar_k(letras, K):
    vistos = set()
    pares = []  # Lista para guardar los pares encontrados
    for x in letras:
        if (K - x) in vistos:
            pares.append((K - x, x))
        vistos.add(x)
    return pares

letras = []
numero = int(input("¿Cuántos números quieres ingresar? "))

for i in range(numero):
    letra = int(input(f"Ingrese el número {i+1}: "))
    letras.append(letra)
K = int(input("Ingresa el valor de K: "))

pares_encontrados = encontrar_k(letras, K)

if pares_encontrados:
    print(f"Se encontraron los siguientes pares cuya suma es {K}:")
    for par in pares_encontrados:
        print(par)
else:
    print(f"No se encontraron pares cuya suma sea {K}.")
