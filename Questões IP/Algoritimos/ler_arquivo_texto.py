
arquivo = open("alunos.txt", "r")

for i, linha in enumerate(arquivo.readlines()):
    
    aluno = linha.strip().split(";") #lista com atributos do aluno
    
    if len(aluno) == 3:
        print("O nome do aluno %d é: %s" % (i+1, aluno[0]))
        print("A idade do aluno é: %d" % int(aluno[1]))
        print("O curso do aluno é: %s" % aluno[2])
        print()


arquivo.close()