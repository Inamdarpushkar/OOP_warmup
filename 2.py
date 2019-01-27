# Pyhton Object Oriented Programming

class Employee:

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+"@company.com"

    def full_name(self):
        return ('{} {}'.format(self.first,self.last))

emp_1=Employee('Chinmay','Deshpande',50000)
emp_2=Employee('Akshay','kulkarni',60000)

#print(emp_1.email)
#print(emp_2.email)

#Different ways
print(emp_1.full_name())
print (Employee.full_name(emp_2))
