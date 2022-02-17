#funções / recursividade
def funcao(i, max):
    if i <= max:
        #print(i, end = " ")
        funcao(i+1, max) #passo recursivo
    
    print("funcao(%d, %d) foi finalizada" 
              % (i, max))

funcao(1, 5)