nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3
if media >= 7.0 <=10:
    print("Parabéns você foi aprovado! Sua média foi: %.2f" %media)
elif media >= 3.0 <=6.9:
    print("Você terá que fazer o exame final. Sua média foi: %.2f" % media )
    if media >= 5 :
        print("Você pode tirar nota maior ou igual a 5 em todas as avaliações e será aprovado")
    else:
        print("Você só será aprovado se tirar notas maiores que 5 em todas avalioções")
else:
    print("Você foi reprovado! Com média: %.2f" %media)