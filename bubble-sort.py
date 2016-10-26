#Algoritmo de Ordenação Bolha
#Bubble Sort


A = [2, 4, 18, 21, 3, 10, 14, 20, 15] # Vetor com os numeros a serem ordenados
size = len(A) # Captura o tamanho do vetor

def ordenarBolha(A):
    for posicao in range(len(A)-1,0,-1):
        for i in range(posicao):
            if A[i]>A[i+1]:
                aux = A[i]
                A[i] = A[i+1]
                A[i+1] = aux
		print(A)

		
ordenarBolha(A)

