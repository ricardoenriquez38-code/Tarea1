def encontrar_k(letras, K):
    n = len(letras)
def encontrar_k(letras, K):
    vistos = set()
    for x in letras:
        if (K - x) in vistos:
            return True
        vistos.add(x)
    return False

letras = []
numero = int(input("¿Cuántos números quieres ingresar? "))

for i in range(numero):
    letra = int(input(f"Ingrese el número {i+1}: "))
    letras.append(letra)

K = int(input("Ingresa el valor de K: "))

resultado = encontrar_k(letras, K)

if resultado:
    print(f"Sí, existe al menos un par cuya suma es {K}.")
else:
    print(f"No, no existe ningún par cuya suma sea {K}.")
