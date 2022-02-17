print("Digite duas datas")
print("Data 1")
d1 = int(input("Digite um dia: "))
m1 = int(input("Digite um mês: "))
a1 = int(input("Digite um ano: "))
print("Data 2")
d2 = int(input("Digite um dia: "))
m2 = int(input("Digite um mês: "))
a2 = int(input("Digite um ano: "))

if a1>a2 or m1>m2 or d1>d2:
    print("A primeira data %d/%d/%d é maior cronologicamente que %d/%d/%d "%(d1, m1, a1, d2, m2, a2))
elif a1==a2 and m1==m2 and d1==d2:
    print("Por favor digite datas diferentes")
else:
    print("A primeira data %d/%d/%d é menor cronologicamente que %d/%d/%d "%(d1, m1, a1, d2, m2, a2))