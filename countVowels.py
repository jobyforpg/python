S1=input("Enter a string")
count=0
for item in S1:
    vow=['a','e','i','o','u']
    for key in vow:
        if(item==key):
            count+=1
print("Number of vowels from you provide word is",count);            
                    
            
