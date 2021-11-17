from math import log,factorial #importa as funções ln e fatorial do módulo math
from statistics import mean # importa a função média do módulo de estatística

x = [0]*10 # cria um vetor com 10 elementos
for i in range(10): # para cada número inteiro entre 0 e 10
    if i%2==0: # caso o número i seja par
        x[i] = 3+7*factorial(i) # o valor do elemento i no vetor x é substituida pela fórmula indicada
    else: #  caso o numero i seja ímpar
        x[i] = 2+4*log(i) # o valor do elemento i no vetor x é substituida pela fórmula indicada
indice_max = n.index(max(x)) # encontra o índice para o elemento máximo de x
valor_medio = round(mean(x),2) # calcula o valor da média dos elementos de x arredondado para duas casas decimais 
print('A posição do maior elemento é', indice_max) 
print('A média dos elementos contidos nesse vetor é', valor_medio)
