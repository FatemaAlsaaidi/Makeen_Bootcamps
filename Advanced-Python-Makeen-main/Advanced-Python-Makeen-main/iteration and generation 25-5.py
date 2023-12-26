import sys
list1=[1,2,3]
print(sys.getsizeof(list1))
for i in list1:
    print(i)

print()

value = iter(list1)
print(sys.getsizeof(value))
print(next(value))


print()

def fun1():
    return 1

def fun2():
    yield 1
    
    
print(fun1())
print(next(fun2()))

def fun3():
     yield 1
     yield 2
     yield 3
     yield 4
     yield 5
value= fun3()

print(next(value))
print(next(value))

print()

for i in value:
    print(i)

print()
    
def fibonacci_numbers(nums):
    x,y=0,1
    for i in range(nums):
        x,y=y,x+y
        yield x
        
        
def square(nums):
    for num in nums:
        yield num**2
        
        
print(sum(square(fibonacci_numbers(10))))
print()

def triple(nums):
    for num in nums:
        yield num**3
        
        
print(sum(triple(square(fibonacci_numbers(10)))))

print()

def even(nums):
    list1=[]
    for i in nums:
        if i%2==0:
            list1.append(i)
    yield list1
a=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]            
print(next(even(a)))

print()

def even(nums):
    list1=[]
    for i in nums:
        if i%2==0:
           yield i
           
           
list1=list(range(1,16))
even=even(list1)
for i in even:
    print(i, end="  ")

    