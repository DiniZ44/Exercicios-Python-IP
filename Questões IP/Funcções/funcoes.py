def soma(n1, n2):
    return n1+n2

def soma2(n1, n2):
    result = n1 + n2
    print("O resultado da soma2 é: %d" % result)

def soma3():
    result = 10 + 30
    return result

def soma4():
    result = 40 + 50
    print("O resultado da soma4 é: %d" % result)


resultado_da_soma = soma(5, 1)
resultado_da_soma2 = soma(10, 2)

print("O resultado da soma é: %d" % soma(20, 30))
soma2(10, 15)
print("O resultado da soma3 é: %d" % soma3())
soma4()

print("O valor da variável resultado_da_soma é %d" % resultado_da_soma)
