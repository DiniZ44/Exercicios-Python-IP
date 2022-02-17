def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n-1)

numero = int(input("Digite um número para descobrir o seu fatorial: "))

print("O fatorial de %d é %d" % (numero, fatorial(numero)))