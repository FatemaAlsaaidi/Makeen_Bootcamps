# Convert Tempreture from C to F 
c_to_f = lambda x:(x*9/5)+32
print(c_to_f(30))

print()
 
# lambda with defualt argument 
summ = lambda a=1, b=2, c=3: a+b+c
print(summ())
print(summ(10))
print(summ(10,20))
print(summ(10,20,30))
print(summ(b=10, c=40))

print()

# Return the number mutiply by 2
multiplication = lambda x: x*2

x1=int(input("Enter number want to multiply by 2: "))

print(x1, "* 2 = ", multiplication(x1))

print()

#Sorted the list of dictionary using lambda
people =[ {'name':'John', 'age':25},
        {'name':'Mary', 'age':23},
        {'name':'Bob', 'age':35},
        {'name':'Alice', 'age':32}
    ]


sorted_list = sorted(people, key=lambda x:x['age'])
print(sorted_list)

print()

people.sort(key=lambda x:x['age'])
print(people)





