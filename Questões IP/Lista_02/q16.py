altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso: "))

if altura < 1.20 :
    if peso <= 60:
        print("Sua classificação é 'A'")
    elif peso >60 and peso < 90:
        print("Sua classificação é 'D'")
    else :
        print("Sua classificação é 'G'")
        
elif altura > 1.20 and altura < 1.70:
    if peso <= 60:
        print("Sua classificação é 'B'")
    elif peso >60 and peso < 90:
        print("Sua classificação é 'E'")
    else :
        print("Sua classificação é 'H'")
        
else:
    if peso <= 60:
        print("Sua classificação é 'C'")
    elif peso >60 and peso < 90:
        print("Sua classificação é 'F'")
    else :
        print("Sua classificação é 'I'")
    