n=int(input("enter number"))
h=0
num=bin(n)[2: ]
l=len(num)
for i in range(l-1):
    h=h+(1<<i)
print(h+1,"is the largest power of 2 lss than",n)


