l1 = []
l2 = []
l3 = []

#cadastrando os elementos da lista 1
cont = 1
while True:
    numero = int(input("Digite o %dº número da lista 1: " % cont))
    
    if numero == -1:
        break
    
    l1.append(numero)
    cont += 1

#cadastrando os elementos da lista 2
cont = 1
while True:
    numero = int(input("Digite o %dº número da lista 2: " % cont))
    
    if numero == -1:
        break
    
    l2.append(numero)
    cont += 1

l3 = l1 + l2

print(l3)