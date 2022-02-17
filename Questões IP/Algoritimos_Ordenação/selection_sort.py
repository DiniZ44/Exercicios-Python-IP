import random
import time

def selectionsort(v):
    
    i = 0
    while i < len(v) - 1:
        menor = i
        
        j = i + 1
        #em busca do menor
        while j < len(v):
            if v[j] < v[menor]:
                menor = j
            j += 1
        
        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp
        
        i += 1
    
    return v

vetor = list(range(0, 10000))

random.shuffle(vetor)

antes = time.time()
vetor_ordenado = selectionsort(vetor.copy())
depois = time.time()
total = depois - antes
print("Tempo total: %f ms" % (total*1000))
#print(vetor_ordenado)
