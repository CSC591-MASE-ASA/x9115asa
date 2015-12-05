from __future__ import division
import math, random, abc

class Optimizer:
    def __init__(self):
        self.print_buffer = []
    @abc.abstractmethod
    def compute(self):
        return None
    def print_output(self):
        for line in self.print_buffer:
            print line

class sa(Optimizer):
    def __init__(self, model):
        self.name='Simulated Annealing'
        self.model = model
    def compute(self):
        Optimizer.__init__(self)
        self.print_buffer.append('Model: '+self.model.name)
        self.print_buffer.append('Optimizer: '+self.name)
        k=0
        kmax = 1000
        s = sb = self.model.get_decision()
        e = eb = self.model.normalize(self.model.energy(s))
        emax = -0.0000001
        op=''
        self.print_buffer.append('e0 = {0:0.2E}'.format(e))
        self.print_buffer.append('s0 = {0}'.format(s))
        self.print_buffer.append('')
        self.print_buffer.append('k     en        eb        output')
        opchar='.'
        def P(old, new, t):
            val = (old-new)/t
            #print math.exp(val)
            return math.exp(val)
        while k < kmax-1 and e > emax:
            sn = self.model.neighbor(s)
            en = self.model.normalize(self.model.energy(sn))
            if k%25==0:
                if op:
                    self.print_buffer.append(op)
                op=''
                op = "{0:04d}, {1:0.2E}, {2:0.2E}, ".format(k, en, eb)
            k+=1
            opchar='.'
            if en < e:
                s, e = sn, en
                opchar= '+'
            elif (P(e, en, 1-k/kmax) > random.random()):
                s, e = sn, en
                opchar= '?'
            if en < eb:
                sb, eb = sn, en
                opchar='!'
            op+=opchar
        self.print_buffer.append('')
        self.print_buffer.append('Final Solution: ')
        self.print_buffer.append('eb = {0:0.2E}'.format(eb))
        self.print_buffer.append('sb = {0}'.format(sb))
        self.print_buffer.append('_'*51)
        self.print_output()
        
        
class mws(Optimizer):
    def __init__(self, model):
        Optimizer.__init__(self)
        self.name='Max Walk Sat'
        self.model = model
    def change_random_c(self, x,c):
        x_old = self.model.normalize(self.model.energy(x))
        x_new = x[:]
        timer = 1000
        no_evals = 0
        x_new[c] = random.uniform(self.model.lower_bounds[c],self.model.upper_bounds[c])
        while timer > 0 and (self.model.eval(x_new) != True):
            x_new[c] = random.uniform(self.model.lower_bounds[c],self.model.upper_bounds[c])
            no_evals += 1
            if self.model.eval(x_new):
                if self.model.energy(x_new) > self.model.min_energy and self.model.energy(x_new) <self.model.max_energy :
                    break
            timer-=1
    
        if self.model.eval(x_new) and self.model.energy(x_new) > self.model.min_energy and self.model.energy(x_new) < self.model.max_energy:
            x_osyczka2 = self.model.normalize(self.model.energy(x_new))
            if x_osyczka2 < x_old:
                return "?", no_evals, x
            elif x_osyczka2 > x_old:
                return "+", no_evals, x_new
            else:
                return ".", no_evals, x
        else:
            return ".", no_evals, x
    def change_c_to_maximize(self, x,c,steps):
        x_best = x[:]
        x_curr = x[:]
        dx = (self.model.upper_bounds[c] - self.model.lower_bounds[c])/steps
        no_evals = 0
        for i in xrange(0,steps):
            no_evals += 1
            x_curr[c] = self.model.lower_bounds[c] + dx*i
            if self.model.energy(x_curr) < self.model.max_energy and self.model.energy(x_curr) > self.model.min_energy:
                if self.model.eval(x_curr) and (self.model.normalize(self.model.energy(x_curr)) > self.model.normalize(self.model.energy(x_best))):
                    x_best = x_curr[:]
    
        # print "RET",x,x_best
        if x==x_best:
            return ".", no_evals, x
        else:
            return "+", no_evals, x_best
    def compute(self):
        self.print_buffer.append('Model: '+self.model.name)
        self.print_buffer.append('Optimizer: '+self.name)
        maxtries=200
        maxchanges=50
        p=0.5
        threshold= 1
        steps=10
        evals = 0
        sb = self.model.get_decision()
        eb = self.model.normalize(self.model.energy(sb))
        self.print_buffer.append('e0 = {0:0.4f}'.format(eb))
        self.print_buffer.append('s0 = {0}'.format(sb))
        self.print_buffer.append('')
        total_evals = 0
        cprob = [0,0,0,0,0,0,0]
        self.print_buffer.append('evals  en      eb      output')
        for i in xrange(0,maxtries):
            solution = self.model.get_decision()
            out = ""
    
            for j in xrange(0,maxchanges):
                stat = ""
                if self.model.normalize(self.model.energy(solution)) > threshold:
                    return solution
    
                c = random.randint(0,self.model.no_of_decisions-1)
                cprob[c] += 1
                if p < random.random():
                    stat, evals, solution = self.change_random_c(solution,c)
    
                else:
                    stat, evals, solution = self.change_c_to_maximize(solution,c,steps)
                esol = self.model.normalize(self.model.energy(solution))
                if  esol >  eb:
                    stat = "!"
                    sb = solution[:]
                    eb = esol
                out += stat
                total_evals += evals
            out="{0:05d}, {1:.4f}, {2:0.4f}, {3}".format(total_evals, esol, eb, out)
            self.print_buffer.append(out)
            out=''
            #print str(self.model.normalize(self.model.energy(sb)))+"\t" +str(self.model.normalize(self.model.energy(solution))) + "\t\t"+out
        
        self.print_buffer.append('')
        
        self.print_buffer.append("Parameters used:\nmaxtries={0}\nmaxchanges={1}\np={2}\nthreshold={3}\nsteps={4}".format(maxtries,maxchanges,p,threshold,steps))
        self.print_buffer.append("Total evaluations: {0}".format(total_evals))
        self.print_buffer.append('Final Solution: ')
        self.print_buffer.append("sb: {0} \neb : {1:0.4f}".format([ '%.2f' % elem for elem in sb ],eb))
        #self.print_buffer.append("cprob: {0}".format(cprob))
        self.print_buffer.append('_'*74)
        self.print_output()
        return eb, sb



    
    
class de(Optimizer):
    def __init__(self, model):
        Optimizer.__init__(self)
        self.name='Differential Evolution'
        self.model=model
    def type1(self, x,y):
        if x <= y:
            return x
        else:
            return y
    def compute(self):
        era_length = 100
        seed = self.model.get_decision()
        cr = 0.3
        f = 0.5
        kmax=1000
        np = era_length
        eras = 5
        k = 0
        def mutate(these):
            sn=[]
            def smear(vals, idx):
                x1 = vals[0] + f*(vals[1]-vals[2])
                if x1 >= self.model.lower_bounds[idx] and x1<=self.model.upper_bounds[idx]:
                    return x1
                else:
                    return vals[random.randrange(0, len(vals)-1)]
            if cr < random.random():
                return these[0]
            for i in xrange(0,len(x)):
                sn = [smear(vals, i) for vals in zip(x,y,z)]
            return sn
    
        def create_frontier(seed):
            frontier = []
            frontier.append(seed)
            for i in xrange(1, np):
                frontier.append(self.model.get_decision())
            return frontier
    
        def generate_items(lst, avoid=None):
            def unique_item():
                x = avoid
                while id(x) in seen:
                  x = lst[  int(random.uniform(0,len(lst))) ]
                seen.append( id(x) )
                return x
    
            assert len(lst) > 4
            avoid = avoid or lst[0]
            seen  = [ id(avoid) ]
            return unique_item(), unique_item(), unique_item()
    
        self.print_buffer.append('Model: '+self.model.name)
        self.print_buffer.append('Optimizer: '+self.name)
        frontier = create_frontier(seed)
        sb = seed
        e = eb = self.model.normalize(self.model.energy(seed))
        self.print_buffer.append('k     ecan      en        eb       output')
        op=''
        while k < kmax :
            for i,candidate in enumerate(frontier):
                e = self.model.normalize(self.model.energy(candidate))
                x, y, z = generate_items(frontier)
                sn=x
                sn = mutate((x,y,z)) #mutate function
                en = self.model.normalize(self.model.energy(sn))
                if k%25==0:
                    if op:
                        self.print_buffer.append(op)
                    op=''
                    op = "{0:04d}, {1:0.2E}, {2:0.2E}, {3:0.2E} ".format(k, e, en, eb)
                out='.'
                if self.model.eval(sn) and en < e:
                    frontier[i] = sn
                    out='+'
                if self.model.eval(sn) and en < eb:
                    sb, eb = sn, en
                    out='!'
                op+=out  
                k = k + 1
        self.print_buffer.append('')
        self.print_buffer.append('Final Solution: ')
        self.print_buffer.append('eb = {0:0.2E}'.format(eb))
        self.print_buffer.append('sb = {0}'.format([ '%.2f' % elem for elem in sb ]))
        self.print_buffer.append('_'*51)
        self.print_output()
        return sb, eb

        
# Given min to max values for every value, try steps of (max - min)/steps for, say, steps=10


# Pseudocode :
# FOR i = 1 to max-tries DO
#   solution = random assignment
#   FOR j =1 to max-changes DO
#     IF  score(solution) > threshold
#         THEN  RETURN solution
#     FI
#     c = random part of solution
#     IF    p < random()
#     THEN  change a random setting in c
#     ELSE  change setting in c that maximizes score(solution)
#     FI
# RETURN failure, best solution found
