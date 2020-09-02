divi=int(input("enter divi"))
dive=int(input("enter dive"))
val=0
q=0
for i in range(31,-1,-1):  #-1 is taken in range to include 0
    if((val+(divi<<i))<=dive):
        val=val+(divi<<i)
        q=q|(1<<i)
print("af division",q)
