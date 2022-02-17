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

for elem in l1:
    if l3.count(elem) == 0:
        l3.append(elem)

for elem in l2:
    if l3.count(elem) == 0:
        l3.append(elem)

print("=== Exibindo as listas ===")
print("Lista 1: ", end = "")
print(l1)
print("Lista 2: ", end = "")
print(l2)
print("Lista 3: ", end = "")
print(l3)