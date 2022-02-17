n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 and n2 > 0:
    res = n1**n2
    print("A elevação dos números é de: %d" %res)
else:
    print("Digite um número maior que zero")
