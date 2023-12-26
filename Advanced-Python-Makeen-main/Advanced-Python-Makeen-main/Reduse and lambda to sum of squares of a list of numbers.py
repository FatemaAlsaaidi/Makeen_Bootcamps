#Calculate the sum of squares of a list of numbers using the reduce()
from functools import reduce

num =[1,2,3]

result= reduce(lambda total,value:total+value**2, num)

print(result)