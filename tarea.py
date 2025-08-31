def encontrar_k(letras, K):
    n = len(letras)
    encontrado = False  
    for i in range(n):
        for j in range(i + 1, n): 
            if letras[i] + letras[j] == K:
                print(f"Par encontrado: {letras[i]} + {letras[j]} = {K}")
                encontrado = True
    return encontrado

letras = []
numero = int(input("¿Cuántos números quieres ingresar? "))

for i in range(numero):
    letra = int(input(f"Ingrese el número {i+1}: "))
    letras.append(letra)
    
K = int(input("Ingresa el valor de K: "))
resultado = encontrar_k(letras, K)

print("¿Existe al menos un par que sume K?", resultado)
