#omega code#
#best case senario#
def fac(n):
    if (n==1) or (n==0):
        return 1
    return n*fac(n-1)
#Time complexity -1 than the code below#
#Space complexity -1 than the code below#
#While n iteration increses time decreases#

#BigO code#
#worst case senario#
def onetoten(n):
    if (n>10):
        return
    print(n)
    onetoten(n+1)
#time complexity +1 than eailier code#
#space complexity +1 than other code#
#while time increases n interation also increses#