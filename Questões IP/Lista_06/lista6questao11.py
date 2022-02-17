def fibo(termo):
    if termo == 0: #ponto de parada
        return 0
    elif termo == 1: #ponto de parada
        return 1
    else:
        return fibo(termo-1) + fibo(termo-2) #passos recursivos

termo = int(input("Digite um número n para descubrir o n-ésimo termo fibonacci: "))

print("O %dº termo da sequência fibonacci é %d." % (termo, fibo(termo)))