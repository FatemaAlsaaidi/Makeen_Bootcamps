#filter positive numbers from lists and positive numbers from lists
numbers = [-4,6,8,-1,3,-5]

positive_list= list(filter(lambda x: x>=0, numbers))
nagetive_list= list(filter(lambda x: x<=0, numbers))

print(positive_list)
print(nagetive_list)


print()
#Using filter and lambda to return the word that lower case in the lists
#and return the word that upper case in the lists

words = ['AAAA','aaaaa','BBBBB','bbbbb','CCCCC','ccccc']

lower_list = list(filter(lambda x:x.islower(), words))
upper_list = list(filter(lambda x:x.isupper(), words))

print(lower_list)
print(upper_list)
