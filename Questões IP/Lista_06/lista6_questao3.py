def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n-1)
def sequencia_fib(i, max):
    if i <= max: #condição de existencia
        print("O fatorial de %d é %d" % (i, fatorial(i)))
        sequencia_fib(i+1, max) #passo recursivo

numero = int(input("Digite um número para descobrir todos os sequencia_fib até o número lido: "))
sequencia_fib(2, numero)