input_file=open("salary and name data.txt","r")
sum_=0
avg=0

dic={}
for line in input_file:
    data=line.rsplit()
    print(data)
    sum_=sum_+float(data[0])
    avg=sum_/len(data[0])
    
    dic[data[1]]=float(data[0])
print()
print("Average of salaries is",avg)
print()
#print(dic)


salaries=[]
for key,value in dic.items():
    salaries.append(value)
    if value==max(salaries):
        print("the  highest salary is,",value, "and the name is",key)
        
#print(salaries)

input_file.close()

try:
    for line in input_file:
        data=line.rsplit()
        print(data)
        sum_=sum_+float(data[0])
   
    
except ValueError:
    print("Non-numeric type entered '%s'" %sum_) 
    
