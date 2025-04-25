#theta: avarage case senario#
n = 10
def function1(n):

   for i in range(0, n+ 1):
      print("First loop")
print("\n", function1(n))
#while n increases time also increses#

#Big O: worst case senario#
j = 1

while j<=n+1:

   print("second loop ", j)

   j = j*2
print("\n", j)
#While j increases time and n increases#

#omega: best case senario#
for i in range(0,100):
    print("third loop")
#While i increases time also increases#