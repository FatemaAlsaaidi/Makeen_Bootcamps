
"""Calculate the Availability of storage the file in the computer"""
memory=int(input("Enter the space of memory="))
size_file=int(input("Enter the size of file="))
number_of_files=int(input("Enter the number of files="))

total_of_size=number_of_files*size_file

if memory>=total_of_size:
    print("It is available")
else:
    print("It is not available")