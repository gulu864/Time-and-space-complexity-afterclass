number1 = int(input("Enter a large number: "))
number2 = int(input("Enter a small number: "))
a = number1
b = number2

while (number2):

    sr = number2
    number2 = number1 % number2
    number1 = sr
hcf = number1

lcm = (a * b) // hcf
print("HCF is ", number1, ".")
print(" And the LCM is", lcm)