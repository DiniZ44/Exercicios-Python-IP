
arquivo = open("alunos.txt", "a") #abertura do arquivo (cria se não existir)

i = 1
while True:
    idade = int(input("Digite a idade do aluno %d: " % i))
    
    if idade < 0:
        break
    
    nome = input("Digite o nome do aluno %d: " % i)
    curso = input("Digite o curso do aluno %d: " % i)
    
    arquivo.write("%s;%d;%s\n" % (nome, idade, curso)) #escrita do arquivo
    i += 1
    
arquivo.close() #fechar o arquivo

