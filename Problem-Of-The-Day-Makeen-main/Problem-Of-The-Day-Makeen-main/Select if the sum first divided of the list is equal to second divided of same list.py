list1 = []

while True:
    num = input("Enter the numer: ")
    if num == "":
        break
    list1.append(int(num))
print(list1)
print()
l1=list1[::-1]

count=0
for i in range(len(list1)):
    if((sum(list1[:i])==sum(list1[i:])) or (sum(l1[:i])==sum(l1[i:]))):
        count=1
    else:
        count=0
if count==1:
    print('True')
else:
    print('False')