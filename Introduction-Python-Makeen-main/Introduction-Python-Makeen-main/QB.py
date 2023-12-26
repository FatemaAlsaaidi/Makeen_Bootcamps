input_file=open("QB.txt","r")
for line in input_file:
    data=data=line.rsplit()
    num=int(data[0])
   
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")
    print()
    