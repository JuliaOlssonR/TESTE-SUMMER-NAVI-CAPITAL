N = 5000000
n = [0]*N
for i in range(1,N+1):
    if i%2==0 and i%49==0 and i%37==0:
        n[i]=1
print('Existem',sum(n),'números pares multiplos de 49 e 37 no intervalo de 1 a 5.000.000 (5 Milhões)')
