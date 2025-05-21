def Rightmost_value(a):
        a = str(a)
    
        if (a[-1] == "1"):
            print("The Rightmost value is 1")
        else:
            print("The Rightmost value isnt 1") 
inp = int(input("Enter a number: "))
binary = bin(inp)
num = binary[2:]
print(num)
Rightmost_value(num)