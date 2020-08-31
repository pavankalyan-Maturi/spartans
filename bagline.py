a=[1,3,2,4,5,3,2]
n=len(a)
bag=0
count=0
i=0
while(i<n):
    if((bag+a[i])<=5):
        bag=bag+a[i]
        i=i+1
    else:
        count=count+1
        print(count,"trip carries bag of",bag)
        print('\n')
        bag=0
print(count+1,"trip carries bag of",bag)

