n=int(input("enter number"))
h=0
num=bin(n)[2: ] #to remove'ob'from the binary repreesentation
l=len(num)      #after removing that then gives the crct length of no. of bits in binary
for i in range(l-1):
    h=h+(1<<i)  #to create n-1 no. of set bits as per our question to ges 2 powers less...
print(h+1,"is the largest power of 2 lss than",n)


