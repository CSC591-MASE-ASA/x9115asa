class Employee:
    # name,age
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    def __lt__(self,other):
        return self.age < other.age;

    def __repr__(self):
        return "Name : {0}, age : {1}".format(self.name,self.age);


e1 = Employee("Alice",25)
e2 = Employee("Dan",22)
e3 = Employee("Bob",20)
employee_list = [e1,e2,e3];
print "Unsorted list: \n",employee_list;

employee_list.sort();
print "Sorted list: \n",employee_list;
