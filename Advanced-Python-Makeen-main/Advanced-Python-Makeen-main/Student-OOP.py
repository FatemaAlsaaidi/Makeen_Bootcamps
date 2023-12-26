from datetime import date
class Person():
    def __init__(self, name, age, address,hours):
        self.name=name
        self.age=age
        self.address=address
        self.hours=hours
    def class_type(self):
        return"This is parent class"

class Student(Person):
     def __init__(self,name, age, address,hours,grade):
         super().__init__(name, age, address,hours)
         self.grade = grade
         
     def class_type(self):
         return"This is student class"
        
     @classmethod
     def new_student(cls,name, brith_year, address,hours,grade):
         return cls(name, date.today().year-brith_year, address,hours,grade)
    
     

s1 = Student("Salim", 23, "Muscat", 100, [3,1,2,5,2])
p1 = Person("Salim", 23, "Muscat", 100)

print(s1.class_type())
print(p1.class_type())
print()
s3 = Student.new_student("Ali", 1993, "Muscat", 100, [3,1,2,5,2])

print(date.today())
print("The age of",s3.name,"is",s3.age)



    
    
       