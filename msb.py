n=int(input("enter number"))
num=bin(n)[2: ]
l=len(num)
h=1<<l-1
print(h,"is the msb")
