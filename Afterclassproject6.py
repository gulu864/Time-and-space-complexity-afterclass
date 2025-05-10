def doublepri(num):
    primen = [True for i in range(num + 1)]

    p = 2
    while (p * p <= num):

        if (primen[p] == True):

            for i in range(p * p, num + 1, p):
                primen[i] = False
        p += 1

    for p in range(11, num + 1):
        if primen[p]:
            print(p)

num = int(input("Enter a number from 11-any: "))
print("Following are the prime numbers smaller than or epuals to ", num)
doublepri(num)