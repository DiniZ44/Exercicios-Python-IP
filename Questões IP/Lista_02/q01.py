nota_1 = float(input("Digite a nota do trabalho de laboratorio: "))
nota_2 = float(input("Digite a nota da avialação semestral: "))
nota_3 = float(input("Digite a nota do exame final: "))

media = (nota_1*2) + (nota_2*3) + (nota_3*5)
res = media/10

if res >= 8.0 <= 10:
    print("Sua média é: %.2f encontra-se no conceito A " % res)
elif res >= 7 <= 7.9:
    print("Sua média é: %.2f encontra-se no conceito B " % res)
elif res >= 6 <= 6.9:
    print("Sua média é: %.2f encontra-se no conceito C " % res)
elif res >= 5 <= 5.9:
    print("Sua média é: %.2f encontra-se no conceito D " % res)
else:
    print("Sua média é: %.2f encontra-se no conceito E " % res)
    
print(res)