from __future__ import division
import math, random,abc

class Model:
    def __init__(self):
        self.no_of_decisions=1
        self.no_of_objecives=2
        self.max_energy = -10**4
        self.min_energy = 10**4
        self.baseline_runs=100000
        self.upper_bounds=[]
        self.lower_bounds=[]
        self.name = 'Generic name'
        
        
    def get_decision(self):
        while True:
            decs =  [random.randrange(self.lower_bounds[dec_number], self.upper_bounds[dec_number])
                     if isinstance(self.lower_bounds[dec_number], int)
                     else random.uniform(self.lower_bounds[dec_number], self.upper_bounds[dec_number])
                     for dec_number in xrange(self.no_of_decisions)]
            if self.eval(decs):
                return decs
    def normalize(self, val):
        return (val - self.min_energy)/(self.max_energy - self.min_energy)
    def neighbor(self, val):
        return self.get_decision()
    def eval(self, decs):
        return True
    def energy(self, decs):
        sum=0
        for val in self.get_objectives(decs):
            sum+=val
        return sum
    @abc.abstractmethod
    def get_objectives(self, decs=[0]):
        return None
    def baseline(self):
        for i in xrange(self.baseline_runs):
            x=self.get_decision()
            f1, f2 = self.get_objectives(x)
            sum = f1+f2
            if sum > self.max_energy:
                self.max_energy=sum
            if sum < self.min_energy:
                self.min_energy = sum

class Schaffer(Model): 
    def __init__(self):
        Model.__init__(self)
        self.upper_bounds=[10000]
        self.lower_bounds=[-10000]
        self.name = 'Schaffer Model'
        
    def get_objectives(self, decs=[0]):
        return decs[0]**2, (decs[0]-2)**2     

class Osyczka2(Model): 
    def __init__(self):
        Model.__init__(self)
        self.no_of_decisions = 6
        self.upper_bounds = [10, 10, 5, 6, 5, 10]
        self.lower_bounds = [0, 0, 1, 0, 1 , 0]
        self.name = 'Osyczka2 Model'
    def eval(self, decs):
        constraints=[]
        constraints.append((decs[0] + decs[1] - 2))
        constraints.append((6 - decs[0] - decs[1]))
        constraints.append((2 - decs[1] + decs[0]))
        constraints.append((2 - decs[0] + 3*decs[1]))
        constraints.append((4 - (decs[2]-3)**2 - decs[3]))
        constraints.append(((decs[4]-3)**2 + decs[5] - 4))
        for constraint in constraints:
            if constraint < 0:
                return False
        return True
    def get_objectives(self, decs=[0,0,0,0,0,0]):
        f1, f2 = 0,0
        f1 = -(25*((decs[0]-2)**2) + (decs[1]-2)**2 + ((decs[2]-1)**2)*((decs[3]-4)**2) + (decs[4] - 1)**2)
        for x in decs:
            f2+=x**2
        return f1, f2
        
class Kursawe(Model): 
    def __init__(self):
        Model.__init__(self)
        self.no_of_decisions=3
        self.upper_bounds = [5,5,5]
        self.lower_bounds = [-5,-5,-5]
        self.name = 'Kursawe Model'
    def get_objectives(self, decs):
        f1, f2 =0,0
        a, b = 0.8, 1
        for i in xrange(self.no_of_decisions-1):
            f1+=(-10*math.exp(-0.2*math.sqrt(decs[i]**2+decs[i+1]**2)))
        for j in decs:
            f2+=(abs(j)**a + 5*math.sin(j))
        return f1, f2
class Golinski(Model):
    def __init__(self):
        Model.__init__(self)
        self.no_of_decisions=7
        self.lower_bounds = [3.5, 0.7, 17.0, 7.3,7.3,2.9,5.0]
        self.upper_bounds = [3.6,0.72,28.0, 8.3,8.3,3.9,5.5]
        self.name = 'Golinski Model'
    def get_decision(self):
        while True:
            decs =  [random.uniform(self.lower_bounds[dec_number], self.upper_bounds[dec_number]) for dec_number in xrange(self.no_of_decisions)]
            if self.eval(decs):
                return decs
    def eval(self, decs):
        constraints=[]
        constraints.append(1/(decs[0]*decs[1]**2*decs[2])-1/27)
        constraints.append(decs[3]**3/(decs[1]*decs[2]**2*decs[5]**4)-1/1.93)
        constraints.append(decs[4]**3/(decs[1]*decs[2]*decs[6]**4)-1/1.93)
        constraints.append(decs[1]*decs[2] - 40)
        constraints.append(decs[0]/decs[1]-12)
        constraints.append(5-(decs[0]/decs[1]))
        constraints.append(1.9 - decs[3] + 1.5*decs[5])
        constraints.append(1.9 - decs[4] + 1.1*decs[6])
        constraints.append((((745*decs[3]/(decs[1]*decs[2]))**2+1.69*10**7)**0.5)/(0.1*decs[5]**3)-1300)
        constraints.append((((745*decs[4]/(decs[1]*decs[2]))**2)+1.575*10**8)**.5/(0.1*decs[6]**3)-1100)
        #print constraints[9]
        for i in xrange(len(constraints)):
            if constraints[i] > 0:
                return False
        return True
    def get_objectives(self, decs=None):
       f1=f2=0
       if decs:
           f1 = 0.7854*decs[0]*decs[1]**2*(10*decs[2]**2/3+14.933*decs[2]-43.0934) - 1.508*decs[0]*(decs[5]**2+decs[6]**2) + 7.477*(decs[5]**3+decs[6]**3)+0.7854*(decs[3]*decs[5]**2+decs[4]*decs[6]**2)
           f2 = (((745*decs[3]/(decs[1]*decs[2]))**2+1.69*10**7)**0.5)/(0.1*decs[5]**3)-1300
       return f1, f2