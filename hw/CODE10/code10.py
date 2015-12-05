from __future__ import division
__author__ = 'Sushil'
from models import Model
import dtlz
import random


class Tuner_Model(Model):
    def __init__(self, lower=[0.01, 50, 100], upper = [0.2, 150, 1000], algo_model=):
        Model.__init__(self)
        #define upper and lower bounds for dec variables: Mutation rate, no of candidates and no of gens
        self.name = 'Tuner Model'
        self.lower_bounds = lower
        self.upper_bounds = upper
        self.no_of_decisions = len(lower)


def differential_evolution(self, model = Tuner_Model):
        era_length = 100
        seed = [0.05, 100, 500]
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
                if x1 >= model.lower_bounds[idx] and x1<=model.upper_bounds[idx]:
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
                frontier.append(model.get_decision())
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
        frontier = create_frontier(seed)
        sb = seed
        e = eb = model.normalize(model.energy(seed))
        while k < kmax :
            for i,candidate in enumerate(frontier):
                e = model.normalize(model.energy(candidate))
                x, y, z = generate_items(frontier)
                sn=x
                sn = mutate((x,y,z)) #mutate function
                en = model.normalize(model.energy(sn))
                if self.model.eval(sn) and en < e:
                    frontier[i] = sn
                if model.eval(sn) and en < eb:
                    sb, eb = sn, en
                    out='!'
                op+=out
                k = k + 1
        return sb


def main():
    seed=[]
    #insert initial call to DE to tune GA here

if __name__ == "__main__":
    main()