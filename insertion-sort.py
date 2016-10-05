#Algoritmo de Ordenação por inserção
#Insertion-Sort


A = [5,2,4,6,1,3] # Vetor com os numeros a serem ordenados
size = len(A) # Captura o tamanho do vetor


currentPosition = 0 #Valor Atual
valueToChange = 0 #Valor a ser trocado

#loop para ler todo o vetor
for i in range (1, size):
    
    valueToInsert = A[i]
    currentPosition = i
    
    #Loop invariante / Verifica se os numeros são maiores que 0 e se são iguais ao da posição corrente do índice do vetor
    while (currentPosition > 0 and A[currentPosition-1] > valueToChange):
        A[currentPosition] = A[currentPosition - 1]
        currentPosition = currentPosition - 1

    A[currentPosition] = valueToChange
print(A) #Imprime os valores ordenados
