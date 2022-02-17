def divisoes(divisor, n):
    if divisor < n:
        if n % divisor == 0:
            return divisor + divisoes(divisor+1, n)
        else:
            return 0 + divisoes(divisor+1, n)
    else:
        return 0
    
def ehPerfeito(n):
    if divisoes(1, n) == n:
        return True
    else:
        return False

numero = int(input("Digite um número para descobrir se é perfeito: "))
        
if ehPerfeito(numero):
    print("O número %d é perfeito" % numero)
else:
    print("O número %d NÃO é perfeito" % numero)