l1=[[0]*4 for i in range(4)]
for i in range(4):
        for j in range(4):
          if (i==j):
            l1[i][j]=1
          elif (i>j):
            l1[i][j]=2
          elif (i<j):
            l1[i][j]=0


for i in range(4):
        for j in range(4):
            print(l1[i][j],end="   ") 
        print()

print()

l2=[[0]*6 for i in range(6)]
for i in range(6):
        for j in range(6):
          if ((i+j)%2==0):
            l2[i][j]=1
            
          elif ((j+i%2!=0)):
            l2[i][j]=0
            
for i in range(6):
        for j in range(6):
            print(l2[i][j],end="   ") 
        print()
        
print()
print()


