n=int(input("enter number"))
num=bin(n)[2: ]  #to remove 'ob'from binary
l=len(num)       #no. of binary bits 
h=1<<l-1         #setting left most bit gives msb
print(h,"is the msb")
