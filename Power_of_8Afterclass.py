n = int(input("Enter a number: "))
bin_n = bin(n)
Bi = bin_n[2:]
print(Bi)

def is_power_of_8(n):
    if n <= 0 or (n & (n - 1)) != 0:
        return False
    position = 0
    while n > 1:
        n >>= 1
        position += 1
    return position % 3 == 0
    

if (is_power_of_8(n)):
    print("The number is the power of 8")
else:
    print("The number is not the power of 8")