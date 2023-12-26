def insertionSort(array):
    
    for step in range(1, len(array)):
        key = array[step]
        j = step -1
        
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j-1
            
            
        array[j +1] = key
        
    return array
l = [5,6,10,1]
print(insertionSort(l))
        