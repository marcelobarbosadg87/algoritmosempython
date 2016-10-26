#Algoritmo de Ordenação Bolha
#Bubble Sort


A = [2, 4, 18, 21, 3, 10, 14, 20, 15] # Vetor com os numeros a serem ordenados
size = len(A) # Captura o tamanho do vetor

#funcao para ordenar // passando o vetor como referencia
def ordenarBolha(A):
    #primeiro laco de interação
    for posicao in range(len(A)-1,0,-1):
        #segundo laco de interação
        for i in range(posicao):
            
            #verifica se a posição é maior que a posicao do próximo numero
            if A[i]>A[i+1]:
                #variavel auxiliar recebe a posicao atual
                aux = A[i]
                #posicao atual recebe o valor da proxima posicao
                A[i] = A[i+1]
                #proxima posicao recebe o valor da posicao atual
                A[i+1] = aux
		#imprime os vetores passo a passo                
		print(A)

		
ordenarBolha(A)

