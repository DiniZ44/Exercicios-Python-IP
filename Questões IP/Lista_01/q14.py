horas = int(input("Digite a quantidade de horas trabalhadas: "))
salario = int(input("Digite o salario minímo: "))

h_trab = salario/2
salario_bruto = h_trab*horas
imposto = salario_bruto*(3/100)
fim = salario_bruto - imposto

print("Seu novo salário é de R$ %d Parabéns!!!!" % fim)