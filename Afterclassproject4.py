number1 = int(input("Enter a number and i'll see if its a palindrome number: "))
original = number1
rev_n = 0

while number1 > 0:
    dig = number1 % 10
    rev_n = rev_n * 10 + dig
    number1 //= 10

if original == rev_n:
    print(original, " is a palindrome number")
else:
    print(original, " is not a palindrome number")