n = int(input("Enter a number: "))

bi = bin(n)
num = bi[2:]
print("Binary value of the given number is: ", num)
rev=0
j = len(num)-1
r_num = num[::-1]
print("Reversed binary value of the given number is: ", num[::-1])
for i in r_num:
    rev = rev+(2**j)*int(i)
    j = j-1
print("Reversed number is", rev)