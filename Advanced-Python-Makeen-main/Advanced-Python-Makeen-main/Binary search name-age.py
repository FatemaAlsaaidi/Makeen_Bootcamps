def insertionSort(array):
    
    for step in range(1, len(array)):
        key = array[step]
        j = step -1
        
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j-1
            
            
        array[j +1] = key
        
    return array

l = ['Said,25','Majid,19', 'Salim,32', 'Ali,21', 'Sultan,28' ]

list1=[]

for i in range( len(l) ):
    age= l[i].split(',')
    list1.append(int(age[1]))
    
print(list1)

slorted_list1=insertionSort(list1)
print(slorted_list1)

list2=[]
list3=[]

for i in range( len(slorted_list1)):
    for j in range(len(l)):
        age= l[j].split(',')
        if slorted_list1[i] == int(age[1]):
            list2.append(l[j])
            list3.append((age[0]))

print(list2)
print(list3)

        
       
    
    







        