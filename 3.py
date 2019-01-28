# Pyhton Object Oriented Programming
#Class variables

class Employee:
    num_of_emps=0
    raise_amount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+"@company.com"

        Employee.num_of_emps+=1

    def full_name(self):
        return ('{} {}'.format(self.first,self.last))

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

emp_1=Employee('Chinmay','Deshpande', 50000)
emp_2=Employee('Akshay','kulkarni',60000)

#emp_2.raise_amount=1.05

emp_1.apply_raise()

#print(emp_1.pay)
print(Employee.raise_amount)
print (emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_2.__dict__)
#print(Employee.__dict__)
