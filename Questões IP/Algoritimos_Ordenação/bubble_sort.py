import random
import time

def bubblesort(v):
    fim = len(v)-1;
    
    while fim > 0:
        i = 0
        while i < fim:
            if v[i] > v[i+1]:
                temp = v[i+1]
                v[i+1] = v[i]
                v[i] = temp
            i += 1
        fim -= 1
    
    return v

vetor = list(range(0, 10000))

random.shuffle(vetor)

antes = time.time()
vetor_ordenado = bubblesort(vetor.copy())
depois = time.time()
total = depois - antes
print("Tempo total: %f ms" % (total*1000))

#print(vetor_ordenado)

