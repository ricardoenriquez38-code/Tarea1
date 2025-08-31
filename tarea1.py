def existe_par_doble_arreglo(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                print(f"Par encontrado: {arr[i]} + {arr[j]} = {K}")
                return True
    return False

# Entrada de datos usando ciclo
arr = []
tamaño = int(input("¿Cuántos números quieres ingresar? "))

for i in range(tamaño):
    num = int(input(f"Ingrese el número {i+1}: "))
    arr.append(num)

K = int(input("Ingresa el valor de K: "))


resultado = existe_par_doble_arreglo(arr, K)
print("¿Existe el par?", resultado)
