#Algoritmo de Ordenação por inserção
#Insertion-Sort


A = [2, 4, 18, 21, 3, 10, 14, 20, 15] # Vetor com os numeros a serem ordenados
size = len(A) # Captura o tamanho do vetor



#loop para ler todo o vetor
for i in range (1, size):
  
    valueToInsert = A[i] #x
    currentPosition = i #j
   
    while (currentPosition >= 0 and valueToInsert < A[currentPosition -1]):
        A[currentPosition] = A[currentPosition -1]
        currentPosition = currentPosition - 1
        
	A[currentPosition] = valueToInsert
    print(A)
print(A) #Imprime os valores ordenados
