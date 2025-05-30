one = int(input("Enter a number: "))
bi = bin(one)
ones = str(bi[2:])
print(ones)

count = 0
for i in ones:
   if i == "1":
      count = count + 1
print(count)