class person:
    num_of_person=0
    def __init__(self,name,age):
        self.name=name
        self.age =age
        person.num_of_person+=1
    '''def descrip(self):
        return f"This person name is {self.name} and{self.age} years old" '''
    
    def __str__(self):
         return"This person name is {} and {} years old".format(self.name,self.age)
    
    def set_age(self,new_age):
        self.__age=new_age

p1=person("Fatema",22)
p2=person("Hamed",30)
#print(p1.descrip())
#print("number of the person",person.num_of_person)
p1.set_age=25
#print(p1.__str__())

print(p1.__str__())



    