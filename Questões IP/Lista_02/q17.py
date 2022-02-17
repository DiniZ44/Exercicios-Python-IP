salario_minimo = float(input("Digite o saláio minímo: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
dependetes = int(input("Digite a quantidade de dependetes: "))
horas_extras = float(input("Digite a quantidade de horas extras: "))

valor_ht =  salario_minimo/5
salario_mes = horas_trabalhadas * valor_ht
valor_depedente = dependetes * 32
valor_hora_extra = (valor_ht * 0.5) + valor_ht
salario_bruto = salario_mes + valor_depedente + valor_hora_extra

if salario_bruto < 200:
    irrf = 0
elif salario_bruto == 200 and salario_bruto < 500:
    irrf = salario_bruto * 0.1 
else:
    irrf = salario_bruto * 0.2 
    
salario_liquido = salario_bruto - irrf

if salario_liquido <= 350:
    gratificacao = salario_liquido + 100
else :
    gratificacao = salario_liquido + 50

salario_receber = salario_liquido + gratificacao
print("O seu salário é de R$ %.2f" %salario_receber)
