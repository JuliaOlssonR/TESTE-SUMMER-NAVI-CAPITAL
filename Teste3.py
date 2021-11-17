dicio = {}
for i in range(5):
    nome = input('Nome do aluno:')
    nota = int(input('Nota:'))
    dicio[nome]= nota
maior_nota = max(dicio,key=dicio.get)
print('O aluno que tirou a maior nota foi',maior_nota,', com nota', dicio[max(dicio,key=dicio.get)])