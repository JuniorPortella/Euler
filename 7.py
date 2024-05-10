count = 0
for x in range(2, 1000000):

    primo = True

    for i in range (2,x):

        if x % i == 0:
            primo = False
            break

    if primo:
        count += 1
    if count == 10001:
        print(x)
        break

