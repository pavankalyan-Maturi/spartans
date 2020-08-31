n=int(input("enter number"))
pos=int(input("postion check  for set"))
if(n&(1<<(pos-1))):
    print(pos,"is set")
else:
    print(pos,"is not set")
