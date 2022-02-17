import random
import time

def shell_sort(v):
    
    h = len(v) // 2
    while h > 0:
        i = h
        while i < len(v):
            trocou = False
            temp = v[i]
            j = i - h
            while j >= 0 and v[j] > temp:
                v[j+h] = v[j]
                trocou = True
                j -= h
            
            if trocou:
                v[j+h] = temp
            
            i += 1
        
        h = h // 2

vetor = list(range(0,100000))
random.shuffle(vetor)

antes = time.time()
shell_sort(vetor)
depois = time.time()

total = (depois - antes) * 1000

#print(vetor)
print("O tempo total foi: %0.2f ms" % total)

