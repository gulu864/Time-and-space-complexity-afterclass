import math

def printPowerset(set,Size):

    Power =(int(math.pow(2, Size)))
    outer = 0
    inner = 0

    for outer in range(1,Power):
        for inner in range(1,Size):
            if ((outer & (1 << inner)) > 1):
                print(set[inner], end = "")
        print("")

word = input("Enter a string ")

set = []
for i in word:
    set.append(i)

print(printPowerset(set, len(set)))