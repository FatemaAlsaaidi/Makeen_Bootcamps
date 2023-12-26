array=[]
counts = {}
while True:
    num = input("Enter the list of number:")
    if num=="":
        break
    array.append(num)
print(array)

for number in array:
    if number not in counts:
      counts[number] = 0
    counts[number] += 1

  # Find the number with the most count.
most_common_number = max(counts, key=counts.get)

  # Print the number with the most count.
print(most_common_number)




    