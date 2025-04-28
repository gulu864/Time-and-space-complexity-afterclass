n = 5

#time complexity is more#
#while n increases time also increases#
def f1(n):
    if(n>0):
        return
    for i in range(0,n+1):
        print("Mathematical")
print(f1(n/2))

#Time complexity is less#
#while n increases time says constant#
def f2(n):
    if (n<=1):
        return
    print("Codingal")
print(f2(n - 1))