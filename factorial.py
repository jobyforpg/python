num=int(input("Enter the number to find factorial"));
fact=1;
if(num<0):
    print("Sorry, factorial does not exist for negative numbers")
elif(num==0):
     
    print("factorial of zero is 1")

else:
    for i in range(1,num+1):
       print(num+1)
       fact*=i
       
print(fact)
