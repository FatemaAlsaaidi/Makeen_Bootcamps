file=open("skip line.txt","r")
for line in file:
    data=line.strip()
    if data!="N/A":
        print(data)
