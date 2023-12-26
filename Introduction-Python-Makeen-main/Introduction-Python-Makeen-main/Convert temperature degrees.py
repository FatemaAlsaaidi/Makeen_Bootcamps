x=int(input("Enter degree:"))
y=input("Enter the type of degree, it is C or F:")

if y=="C":
    r1=(x*(9/5))+32
    print(r1)
elif y=="F":
    r2=((x-32)*5)/9
    print(2)
else:
    print("Ther is an error")
