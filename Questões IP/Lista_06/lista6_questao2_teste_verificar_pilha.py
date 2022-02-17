#verificando que a recursividade trabalha na forma de PILHA

def fatorial(n):
    if n == 1 or n == 0:
        print("Terminando a execução de fatorial(%d)" 
              % n)
        return 1
    else:
        resultado = n * fatorial(n-1)
        print("Terminando a execução de fatorial(%d)" 
              % n)
        return resultado

numero = int(input("Digite um número para descobrir o seu fatorial: "))

print("O fatorial de %d é %d" % (numero, fatorial(numero)))