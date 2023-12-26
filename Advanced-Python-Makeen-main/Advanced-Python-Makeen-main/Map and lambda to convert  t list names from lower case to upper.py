#Using Map and lambda to conver t list names from lower case to upper case
name_list=[]

while True:
    name = input("Enter name: ")
    if name =="":
        break
    name_list.append(name)
print(name_list)

convert = list(map(lambda x:x.upper(), name_list))

print(convert)