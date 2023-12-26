List_=[22,3,-2,-1,10,1]

multi=1
count=0

for i in List_:
    #printing all elements of a list in as single row , separated by space 
    print(i,"  " ,end='')
    #computing of product of all elements in a list
    multi = multi * i
    #Counting how many elements in a list are negative
    if i<0:
        count=count+1

print()
print()

print("The computing of product of all elements is"," ",multi)

print()

print("The number of negative number in list is"," ",count)
    
    
    
    
