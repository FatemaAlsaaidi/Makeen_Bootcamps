input_file=open("QA.txt","r")
for line in input_file:
    data=data=line.rsplit()
    #print(data)
    
    speed=int(data[0])*int(data[1])
    print("The distence is:",speed)