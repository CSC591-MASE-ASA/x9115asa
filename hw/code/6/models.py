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
            decs =  [random.randrange(self.lower_bounds[dec_number], self.upper_bounds[dec_number]) for dec_number in xrange(self.no_of_decisions)]
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
