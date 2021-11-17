N = 5000000
n = [0]*N # cria uma lista de zeros de comprimento equivalente a quantidade de números inteiros entre 1 e 5000000
for i in range(1,N+1): # analisa cada número no intervalo de 1 a 5000000
    if i%2==0 and i%49==0 and i%37==0: # verifica se o número em questão cumpre os requisitos
        n[i]=1 # satisfazendo as condições, o valor do elemento i de n é substituido por 1
total = sum(n) # soma a quantidade de números que satisfizeram os requisitos
print('Existem',total,'números pares multiplos de 49 e 37 no intervalo de 1 a 5.000.000 (5 Milhões)')
