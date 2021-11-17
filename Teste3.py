dicio = {} # cria um dicionário
for i in range(5): # loop para fazer os inputs dos dados de 5 alunos
    nome = input('Nome do aluno '+str(i+1)+':') # input para inserir o nome do aluno
    nota = float(input('Nota do aluno '+str(i+1)+':')) # input para inserir a nota do aluno
    dicio[nome]= nota #cria a chave com o nome do aluno no dicionário cujo valor é a nota do aluno
maior_nota = max(dicio,key=dicio.get) # encontra a chave que tem o maior valor do dicionário

print('O aluno que tirou a maior nota foi',maior_nota,', com nota', dicio[max(dicio,key=dicio.get)]) # imprime o aluno com a maior nota e a respectiva nota que ele tirou
