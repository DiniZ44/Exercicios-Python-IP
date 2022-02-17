n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
n3 = int(input("Digite um terceiro número: "))

if n2 >= n1 <=n3 > n2:
    print ("O número %d é menor. O número %d é o maior. "%(n1, n3))
elif n2 >= n1 <=n3 < n2:
    print ("O número %d é menor. O número %d é o maior."%(n1, n2))
elif n1 >= n2 <=n3 > n1:
    print ("O número %d é menor. O número %d é o maior. "%(n2, n3))
elif n1 >= n2 <=n3 < n1:
    print ("O número %d é menor. O número %d é o maior. "%(n2, n1))
elif n1 >= n3 <=n2 > n1:
    print ("O número %d é menor. O número %d é o maior."%(n3, n2))
else :
    print ("O número %d é menor. O número %d é o maior. "%(n3, n1))
