word=input("ENTER A WORD")
vow_list=[]
for item in word:
    vow=['a','e','i','o','u']
    for key in vow:
        if(item==key):
            values=key
            vow_list.append(values)
print(vow_list)
