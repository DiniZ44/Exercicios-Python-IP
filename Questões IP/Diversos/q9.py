
soma_peso1,soma_peso2,soma_peso3,soma_peso4 = 0,0,0,0
qtd_1,qtd_2,qtd_3,qtd_4 = 0,0,0,0

maximo_pessoas = 15
i= 1
t = 1
v = 1
while i <= maximo_pessoas:
    idade = float(input("Digite a idade %d pessoa: " % i))
    peso = int(input("Digite o peso da %d pessoa: " % i))


    if idade > 1 and idade <= 10:
        soma_peso1+=peso
        qtd_1+=1



    elif idade >= 11 and idade <= 20:
        soma_peso2 += peso
        qtd_2 += 1


    elif idade >= 21 and idade <= 30:
        soma_peso3 += peso
        qtd_3 += 1


    else:
        soma_peso4 += peso
        qtd_4 += 1

    i += 1

#um pequeno tratamento de erro de forma bem simples
if soma_peso1 != 0:
     print("A media de pesos entra pessoas de 1 a 10 anos e %.2f" % (soma_peso1/ qtd_1))
if soma_peso2 != 0:
    print("A media de pesos entra pessoas de 11 a 20 anos e %.2f" % (soma_peso2 / qtd_2))
if soma_peso3 != 0:
    print("A media de pesos entra pessoas de 21 a 30 anos e %.2f" % (soma_peso3 / qtd_3))
if soma_peso4 != 0:
    print("A media de pesos com mais de 31 anos e %.2f" % (soma_peso4 / qtd_4))





