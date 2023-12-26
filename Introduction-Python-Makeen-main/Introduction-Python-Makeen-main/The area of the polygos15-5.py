import math
def area(n, s):
    a=(n*(s**2))/(4*math.tan(math.pi/n))
    return a
n=int(input("Enter the number of sides:"))
s=float(input("Enter the side:"))

area_=area(n,s)
print("The area of the polygos is ",area_)

