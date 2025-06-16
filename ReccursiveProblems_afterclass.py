n = int(input("Enter a number: "))

def powerof(n):
    
    if (n <= 0 ):
        return False
    if (n == 1):
        return True
    if (n%2 == 0):
        return powerof(n/2)
    return False

if (powerof(n)):
    print("The number is a power of 2")
else:
    print("The number is not the power of 2")