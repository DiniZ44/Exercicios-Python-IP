def fat(n):
    if n == 1 or n == 0:
        return 1
    else:
       return fat(n-1) * n

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def entrada(i,f):
    if(f > i):
        entrada(i,f-1)
    print ("O fatorial de %d eh: %d "%(f,fat(f)))

def entrada1(i,f):
    if(f > i):
        entrada1(i,f-1)
    print ("O fibonacci de %d eh: %d "%(f,fib(f)))

print ("\n\t----FATORIAL----\n")
x = int(input("Digite um numero inicial !"))
z = int(input("Digite um numero final !"))
print("\n")
entrada(x,z)

print ("\n\t----FIBONACCI----\n")
x = int(input("Digite um numero inicial !"))
z = int(input("Digite um numero final !"))
print("\n")
entrada1(x,z)

def entrada2(n):
    if(n > 0):
        entrada1(n-1)
    print ("O fibonacci de %d eh: %d "%(n,fib(f)))
