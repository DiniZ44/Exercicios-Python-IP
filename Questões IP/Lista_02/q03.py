print("Digite três números diferentes!")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n2!=n3 and n3!=n1 and n1!=n2:
    if n2 > n1 <n3 > n2:
        print ("%d, %d, %d "%(n1, n2, n3))
    elif n2 > n1 <n3 < n2:
        print ("%d, %d, %d "%(n1, n3, n2))
    elif n1 > n2 <n3 > n1:
        print ("%d, %d, %d "%(n2, n1, n3))
    elif n1 > n2 <n3 < n1:
        print ("%d, %d, %d "%(n2, n3, n1))
    elif n1 > n3 <n2 > n1:
        print ("%d, %d, %d "%(n3, n1, n2))
    else:
        print ("%d, %d, %d "%(n3, n2, n1))
        
else:
    print("Somente números diferentes são aceitos!")
