

#essa versao da funcao recebe como argumentos
#os valores das matrizes nas posicoes i,j, bem como
#os indices de i,j.
#a funcao armazena o resultado na matriz
#result, passada por referencia
def add(val1, val2, i, j, result):
  result[i][j] = val1 + val2
  
def unroll(args, func, method, res):
  #itera em todas as linhas da matriz de argumentos
  for i in range(len(args)):
    #para o trabalho vcs tem que executar cada chamada de func
    #em paralelo
    func(*args[i], *res[i])

matA = [[1,2],
        [3,4]]
matB = [[5,6],
        [7,8]]

#versao sequencial da soma
matC = [[0 for i in range(2)] for i in range(2)]
for i in range(2):
  for j in range(2):
    matC[i][j] = matA[i][j] + matB[i][j]
print("matriz c " + str(matC))

#dessa versao sequencial tiramos que func precisa
#receber como argumentos: os elementos a serem somados,
#as posicoes dos elementos nas matrizes e uma matriz para
#armazenar os resultados. Dai escrevemos a funcao add, acima.


#versao usando unroll
#Primeiro precisamos construir a matriz args.
#A minha funcao func(add) recebe como argumentos
#o valor dos elementos da matriz, bem como os indices
#onde a função deve armazenar o resultado. Assim:
args = [ [1, 5, 0, 0],
         [2, 6, 0, 1],
         [3, 7, 1, 0],
         [4, 8, 1, 1]]

#Depois construir a matriz result.
#Nesse caso, todas as chamadas de func devem armazenar 
#o resultado na matriz matC_unroll. Aqui usamos o fato de 
#python usar referencias ao inves de valores para 
#passar matC_unroll 4 vezes, uma para cada chamada de func
matC_unroll = [[0 for i in range(2)] for i in range(2)]

results = [[matC_unroll],
           [matC_unroll],
           [matC_unroll],
           [matC_unroll]]

#chamada de func para o caso da soma
unroll(args, add, 'whatever', results)
print("Mat C after unroll")
print(matC_unroll)
