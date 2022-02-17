notas = []
QNT_NOTAS = 5

i = 1 #contador
soma = 0 #acumulador

while i <= QNT_NOTAS:
    nota = float(input("Digite a %dª nota: " % i))
    notas.append(nota)
    
    soma += nota
    i += 1

média = soma/QNT_NOTAS

print("A média é: %.2f" % média)