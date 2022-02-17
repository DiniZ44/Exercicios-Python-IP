LINHAS = 20

'''vetor = []

i = 0
while i < LINHAS:
    numero = int(input("Digite o %dº número inteiro: " % (i+1)))
    vetor.append(numero)
    i += 1'''

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

pares = []
impares = []

for i, elemento in enumerate(vetor):
    if elemento % 2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)


print("Vetor com todos os números: ")
for i, elemento in enumerate(vetor):
    print("O elemento do índice %d é %d." % (i, elemento))

print("==============\n")

print("Vetor de números pares: ")
for i, par in enumerate(pares):
    print("O elemento do índice %d é %d." % (i, par))

print("==============\n")

for i, impar in enumerate(impares):
    print("O elemento do índice %d é %d." % (i, impar))





