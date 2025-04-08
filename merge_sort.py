def merge_sort(vetor):
    if len(vetor) > 1:
        meio = len(vetor) // 2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        
        merge_sort(esquerda)
        merge_sort(direita)

        
        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1

# Programa principal
if __name__ == "__main__":
    vetor = []

    print("Digite 8 números:")
    for _ in range(8):
        numero = int(input("Número: "))
        vetor.append(numero)

    merge_sort(vetor)

    print("Vetor ordenado:")
    print(vetor)