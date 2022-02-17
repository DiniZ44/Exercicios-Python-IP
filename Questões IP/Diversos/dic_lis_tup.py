'd = dict()'


d = {}
d['cabra'] = 45
d['vaca'] = 1600.00
d['ovelha'] = 190
d['boi'] = 2800.00

d = {'cabra': 45 , 'vaca': 1600.00 , 'ovelha': 190 , 'boi': 2800.00}

#CASO EU QUEIRA MOSTRA SÓ O ANIMAL      #for chave in(d.keys()): #list or tuple  d.keys
                                            #print(chave)
    
#CASO EU QUEIRA MOSTRA SÓ O VALOR      # for valor in(d.values()):  #list or tuple  d.values
                                            # print(valor)
    
#CASO EU QUEIRA MOSTRA OS DOIS:  
for chave, valor in list(d.items()):   #list or tuple  d.items
    print("Animal: %s / Valor: %.2f" %(chave, valor))


