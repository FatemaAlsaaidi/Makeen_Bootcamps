x=[[1,2,3],
   [4,5,6]]
for i in x[0]:
    print(i,end="")   
print()


for i in x:
    print(i[0],end="")    
print()

for i in range(2):
    for j in range(3):
        print(x[i][j],end="")
    print()
print()


for i in range(2):
    
    for j in range(1):
        print("[", end=" ")
        
    for j in range(3):
        print(x[i][j], end=" ")
    
    for j in range(1):
        print("]", end="")
        
    print()
    
print()


for i in range (3):    
     for j in range(3):
        print(i+1, end="  ")
     print()
print()


l=[[i]*3 for i in range (1,4)]
for i in range (3):
    for j in range(3):
        print(l[i][j], end="  ")
    print()
print()


x=[i+1 for i in range (3) for j in range(3)]
print(x)
print()

x=int(input("Enter numbers:"))
for i in range (3):
     x=x+1
     for j in range(3):
        print(x, end="  ")
     print()
print()


