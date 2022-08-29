# Shallow copy: one level deep, only references of nested objects
# Deep copy: full independent copy

#import copy
#
## shallow copy
#org = [0, 1, 2, 3, 4]
#
#cpy = copy.copy(org)
##cpy = org.copy()
##cpy = org[:]
#
#cpy[0] = -10
#print(org)
#print(cpy)
#
## deep copy 
#org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
#
#cpy = copy.deepcopy(org)
#
#cpy[0][0] = -10
#print(org)
#print(cpy)

##############################
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee



p1 = Person('Alex', 27)
p2 = Person('Joe', 55)

company = Company(p1, p2)

company_clone = copy.deepcopy(company)
company_clone.boss.age = 60 


print(company_clone.boss.age)
print(company.boss.age)




