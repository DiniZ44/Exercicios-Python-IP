#repetição / iteração
''''i = 1
while i <= 10:
    print(i, end = " ")
    i += 1

print("")'''

#funções / recursividade
def funcao(i, max):
    if i <= max: #condição de existência
        print(i, end = " ")
        funcao(i+1, max) #passo recursivo

funcao(1, 10)