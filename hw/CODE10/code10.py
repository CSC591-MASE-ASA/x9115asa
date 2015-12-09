from __future__ import division
__author__ = 'Sushil'
from models import Model
import dtlz
from code9 import *
import random


class Tuner_Model(Model):
    def __init__(self, lower=[0.01, 50, 100], upper = [0.2, 150, 1000], algo_model=dtlz.dtlz1, algo_num_obj=1, algo_num_decs=1):
        Model.__init__(self)
        #define upper and lower bounds for dec variables: Mutation rate, no of candidates and no of gens
        self.name = 'Tuner Model'
        self.lower_bounds = lower
        self.upper_bounds = upper
        self.no_of_decisions = len(lower)
        self.algo_model = algo_model
        self.algo_num_obj = algo_num_obj
        self.algo_num_decs = algo_num_decs
    def energy(self, s):
        ga = GA(self.algo_model, self.algo_num_obj, self.algo_num_decs, *s)
        hve1 = ga.run()
        return hve1.hyper_vol

def differential_evolution(model = Tuner_Model()):
        cr = 0.3
        f = 0.5
        kmax=3
        np = 15
        seed = model.get_decision()
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
        eb = model.energy(seed)
        print eb
        print 'Best energy so far: '+str(eb)
        print 'Best solution so far: '+str(sb)
        no_change=0
        for k in xrange(kmax):
            for i,candidate in enumerate(frontier):
                e = model.energy(candidate)
                x, y, z = generate_items(frontier)
                sn = mutate((x,y,z)) #mutate function
                en = model.energy(sn)
                if en > e:
                    frontier[i] = sn
                if en > eb:
                    no_change=0
                    sb, eb = sn, en
                if eb > 0.999 and no_change > 10:
                    return sb
                print 'Best energy so far: '+str(eb)
                print 'Best solution so far: '+str(sb)
        return sb


def main():
    seed=[]
    #insert initial call to DE to tune GA here
    #define upper/lower limits for mutation rate, no candidates and no gens
    models = [dtlz.dtlz1, dtlz.dtlz3, dtlz.dtlz5, dtlz.dtlz7]
    objs = [2, 4, 6, 8]
    decs = [10, 20, 40]
    lower = [0.01, 50, 500]
    upper = [0.5, 100, 1000]
    rdiv_ip=[]
    for model in models:
        for num_objs in objs:
            for num_decs in decs:
                run_name = model.__name__+'_o'+str(num_objs)+'_d'+str(num_decs)
                print run_name
                tm = Tuner_Model(lower, upper, model, num_objs, num_decs)
                ga_params = differential_evolution(tm)
                tune = [run_name+'_t']
                untune = [run_name+'_u']
                for i in xrange(20):
                    ga_t = GA(model, num_objs, num_decs, *ga_params)
                    res_t = ga_t.run()
                    tune.append(res_t.hyper_vol)
                    ga_u = GA(model, num_objs, num_decs, prob_mut=0.05, num_candidates=100, num_generations=1000)
                    res_u = ga_u.run()
                    untune.append(res_u.hyper_vol)
                rdiv_ip.append(tune)
                rdiv_ip.append(untune)
                print rdiv_ip
if __name__ == "__main__":
    main()