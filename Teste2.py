from math import log,factorial
from statistics import mean

x = [0]*10
for i in range(10):
    if i%2==0:
        x[i] = 3+7*factorial(i)
    else:
        x[i] = 2+4*log(i)
print('A posição do maior elemento é', n.index(max(n)))
print('A média dos elementos contidos nesse vetor é',round(mean(n),2))