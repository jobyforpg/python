n=int(input("Enter the number of term"))
f1=0
f2=1
sum=0; count=1
while(count<=n):
    print(sum,"")
    count+=1
    f1=f2
    f2=sum
    sum=f1+f2
