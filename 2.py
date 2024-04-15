
ant1 = 0
ant2 = 1
som = 0
for x in range(100):

    prox = ant1 + ant2

    ant1 = ant2
    ant2 = prox

    if(ant2<4000000):
        if(ant2 % 2 == 0):
            som += ant2
    


print(som)