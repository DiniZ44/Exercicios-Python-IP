def fibo(termo):
    if termo == 0: #ponto de parada
        return 0
    elif termo == 1: #ponto de parada
        return 1
    else:
        return fibo(termo-1) + fibo(termo-2) #passos recursivos

def sequencia_fibo(i, max):
    if i <= max: #condição de existencia
        print("%d" % fibo(i), end=" ")
        sequencia_fibo(i+1, max) #passo recursivo

termo = int(input("Digite um número n para descobrir a sequência fibonacci até esse n-ésimo termo: "))
        
sequencia_fibo(0, termo)