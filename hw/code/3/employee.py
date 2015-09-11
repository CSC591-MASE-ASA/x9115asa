class Employee:
    # name,age
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    def __lt__(self,other):
        return self.age < other.age;

    def __repr__(self):
        return "Name : {0}, age : {1}".format(self.name,self.age);


e1 = Employee("Abc",25)
e2 = Employee("Def",22)
e3 = Employee("Hij",20)
employee_list = [e1,e2,e3];

print employee_list;

employee_list.sort();
print "Sorted: ",employee_list;
