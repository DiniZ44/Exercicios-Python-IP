LINHAS = 2
COLUNAS = 3

alunos = [] #matriz de alunos com notas


#ler as informações de todos os alunos
i = 0
while i < LINHAS:
    
    
    nome = input("Digite o nome do aluno %d: " % (i+1))
    cpf = input("Digite o CPF do aluno %d: " % (i+1))
    notas = []
    
    _aluno = {
                "nome": nome,
                "cpf": cpf,
                "notas": notas
            }
    
    alunos.append(_aluno)
    
    #ler as tres notas do aluno i
    j = 0
    while j < COLUNAS:
        nota = float(input("Digite a %dª nota do aluno %d: "
                           % (j+1, i+1)))
        alunos[i]["notas"].append(nota)
        
        j += 1 #indo para a próxima nota
    
    i += 1 #indo para o próximo aluno


alunos = [{'notas': [6.0, 7.0, 8.0], 'nome': 'Ygor', 'cpf': '123'}, {'notas': [8.0, 7.0, 4.0], 'nome': 'Israel', 'cpf': '7'}]


for i, aluno in enumerate(alunos):
    print("Detalhamento do aluno %d:" % i)
    
    print("\tNome: %s" % aluno["nome"])
    print("\tCPF: %s" % aluno["cpf"])
    print("\tNotas: ", end="")
    
    for nota in aluno["notas"]:
        print("%.2f " % nota , end="")
    
    print("")










      