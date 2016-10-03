#Algoritmo de Ordenação por inserção
#Insertion-Sort

A = [5,2,4,6,1,3]
size = len(A)

#Valor Atual
currentPosition = 0
#Valor a ser trocado
valueToChange = 0

#loop para ler todo o vetor
for i in range (1, size):
    
    valueToInsert = A[i]
    currentPosition = i
    
    #Loop invariante
    while (currentPosition > 0 and A[currentPosition-1] > valueToChange):
        A[currentPosition] = A[currentPosition - 1]
        currentPosition = currentPosition - 1

    A[currentPosition] = valueToChange
print(A)
