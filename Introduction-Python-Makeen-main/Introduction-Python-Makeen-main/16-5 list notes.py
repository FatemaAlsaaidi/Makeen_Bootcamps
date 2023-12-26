x=[1,2,3,4,5]
x.extend([5,6,7])
print(x)

x=str([3,4,5])

for i in x:
    "|".join(x)
    print(x)

result=[]
for i in range(5):
    result.append(i**2)
print(result)

result_=[]
result_=[i**2 for i in range(5)]
print(result_)

result=[]
result=[i for i in range(5) if (i%2==0) ]
print(result)