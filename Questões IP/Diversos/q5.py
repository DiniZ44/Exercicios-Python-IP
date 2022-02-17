ant1 = 0
ant2 = 1

print("0 e 1", end = "  " )

fib = ant1 + ant2
while fib <= 2584:
    print("%d"% fib, end = "  ")
    ant1 = ant2
    ant2 = fib
    fib = ant1 + ant2