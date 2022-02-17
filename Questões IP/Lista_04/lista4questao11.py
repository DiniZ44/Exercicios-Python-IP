'''
11) Faça um programa que preencha uma matriz 10 × 3 com as notas de
dez alunos em três provas. O programa deverá mostrar um relatório com
o número dos alunos (número da linha) e a prova em que cada aluno obteve
menor nota. Ao final do relatório, deverá mostrar quantos alunos tiveram
menor nota em cada uma das provas: na prova 1, na prova 2 e na prova 3. '''

LINHAS = 10
COLUNAS = 3

alunos = [] #matriz de alunos com notas
piores_provas = []

#contadores de piores provas
qnt_alunos_p_prova1 = 0
qnt_alunos_p_prova2 = 0
qnt_alunos_p_prova3 = 0

#ler as informações de todos os alunos
i = 0
while i < LINHAS:
    alunos.append([])
    
    #ler as tres notas do aluno i
    j = 0
    while j < COLUNAS:
        nota = float(input("Digite a %dª nota do aluno %d: "
                           % (j+1, i+1)))
        alunos[i].append(nota)
        
        if j == 0:
            menor = nota
            indice_menor = 0
        elif nota < menor:
            menor = nota
            indice_menor = j
        
        j += 1 #indo para a próxima nota
    
    piores_provas.append(indice_menor)
    
    if indice_menor == 0:
        qnt_alunos_p_prova1 += 1
    elif indice_menor == 1:
        qnt_alunos_p_prova2 += 1
    else:
        qnt_alunos_p_prova3 += 1
    
    i += 1 #indo para o próximo aluno

i = 0
while i < LINHAS:
    print("O aluno %d teve sua pior nota na prova %d" % 
          (i+1, piores_provas[i]+1))
    i += 1

print("%d alunos tiveram o pior desempenho na prova 1."
      % qnt_alunos_p_prova1)
print("%d alunos tiveram o pior desempenho na prova 2." 
      % qnt_alunos_p_prova2)
print("%d alunos tiveram o pior desempenho na prova 3."
      % qnt_alunos_p_prova3)













      