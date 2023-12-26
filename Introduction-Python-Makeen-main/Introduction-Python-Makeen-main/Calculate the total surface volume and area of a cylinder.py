""" Q1: Write a python program to calculate the total surface volume and area of a cylinder """
r=int(input("Enter the value of radius:"))
h=int(input("Enter the value of Height:"))
pi=3.14
v = pi*r**2*h
print("The value of volume is", v)
area=(2*pi*r*h) + (2*pi*r**2)
print("The value of area is", area)

