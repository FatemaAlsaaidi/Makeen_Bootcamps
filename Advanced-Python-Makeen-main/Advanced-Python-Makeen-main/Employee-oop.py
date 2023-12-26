class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        
    def calculate_emp_salary(self,salary,hours):
        overtime=hours-50
        if hours > 250:
            self.emp_salary=salary+overtime
        else:
             self.emp_salary=salary
        
 
    def assign_department(self,new_emp_department): ##enable to change
        self.emp_department=new_emp_department
        
    #def __str__(self):return"This person name is {}, his/her id is {}".format(self.emp_name,self.emp_id)"""
    def emp_delails(self):
         return"Name:{}, ID: {}, Salary: {} Department: {}".format(self.emp_name,self.emp_id,self.emp_salary,self.emp_department)
        
   
        
   

E1 =Employee(1,"Fatema",200,"IT")
E2 =Employee(2,"Noor",500,"Math")
#print(employee1) #<__main__.Employee object at 0x0000021ADC7BF5E0>

#print(employee1.__str__())

E1.assign_department('Engineering')
E2.assign_department('doctor')


print(E1.emp_delails())

print(E2.emp_delails())