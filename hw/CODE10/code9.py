import dtlz
import random
import math
import hve
import cProfile
class candidate:
    num_objs = 10

    def __init__(self, decs):
        self.decs = decs
        self.fitness = None
        self.dom_count = 0

    def calc_fitness(self, fitness_family):
        self.fitness = fitness_family(self.decs, candidate.num_objs, len(self.decs))
        return

    def __gt__(self, other):
        if self.fitness == other.fitness:
            return False
        for i in xrange(candidate.num_objs):
            if other.fitness[i] < self.fitness[i]:
                return False
        return True

    def __repr__(self):
        return 'Candidate: ['+",".join([str(x) for x in self.decs])+']\n'


class population:
    num_candidates = 10;
    fitness_family = None
    prob_mut = 0.05
    num_decs = 2

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1):
        self.candidates = []
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family
        self.pop_pareto = []

    def randomize(self):
        for i in range(self.num_candidates):
            can = candidate([])
            for j in range(self.num_decs):
                can.decs.append(random.random())
            can.calc_fitness(self.fitness_family)
            self.candidates.append(can)
        self.ap_binary_dom()

    def crossover(self, candidate1, candidate2):
        crossover_point = random.randrange(0, self.num_decs)
        decs1 = []
        decs2 = []
        for i in xrange(crossover_point):
            decs1.append(candidate1.decs[i])
            decs2.append(candidate2.decs[i])
        for i in xrange(crossover_point, self.num_decs):
            decs1.append(candidate2.decs[i])
            decs2.append(candidate1.decs[i])
        can1 = candidate(decs1)
        can1.calc_fitness(self.fitness_family)
        can2 = candidate(decs2)
        can2.calc_fitness(self.fitness_family)
        return [can1, can2]

    def mutate(self, candidate):
        for i in xrange(self.num_decs):
            if random.random() < self.prob_mut:
                candidate.decs[i] = random.random()

    def __repr__(self):
        return ",".join([can.__repr__() for can in self.candidates])

    def ap_binary_dom(self):
        candidates = self.candidates
        n = self.num_candidates
        for candidate1 in candidates:
            can_dominates_all = True
            for candidate2 in candidates:
                if candidate2 > candidate1:
                    can_dominates_all = False
                    break
            if can_dominates_all:
                self.pop_pareto.append(candidate1)

    #def weighted_wheel(self):
    #    # weighted wheel technique of selection
    #    sumTemp = sum([x.dom_count for x in self.candidates])
    #    if sumTemp == 0:
    #        return self.candidates[random.randint(0, self.num_candidates-1)]
    #    rand = random.random()*sumTemp
    #    sumT = 0
    #    for i in xrange(self.num_candidates):
    #        sumT += self.candidates[i].dom_count
    #        if rand < sumT:
    #            return self.candidates[i]

class GA:
    fitness_family = None
    num_candidates = 100
    def __init__(self, fitness_family=dtlz.dtlz1, num_objs=2, num_decs=10, prob_mut=0.05, num_candidates=100, num_generations=1000):
        self.generations = []
        self.current_generation = 0
        self.num_candidates = int(num_candidates)
        self.fitness_family = fitness_family
        self.num_generations = int(num_generations)
        self.pareto_frontier = []
        candidate.num_objs = num_objs
        population.num_decs = num_decs
        population.prob_mut = prob_mut

    def randomize(self):
        gen1 = population(self.num_candidates, self.fitness_family)
        gen1.randomize()
        self.generations.append(gen1)
        self.pareto_frontier.extend(gen1.pop_pareto)
        return
    def update_pareto(self, new_pareto):
        add_new = []
        for new in new_pareto:
            for old in self.pareto_frontier:
                if new > old:
                    self.pareto_frontier.remove(old)
                if not old > new and not old==new:
                    add_new.append(new)
                    break
        self.pareto_frontier.extend(add_new)
    def next(self):
        curr_pop = self.generations[self.current_generation];
        next_pop = population(self.num_candidates, self.fitness_family)
        for i in range(0, self.num_candidates, 2):
            #print(self.pareto_frontier)
            pareto_idx=[0,0]
            if len(self.pareto_frontier) >= 2:
                pareto_idx = random.sample(xrange(len(self.pareto_frontier)), 2)
            can1 = self.pareto_frontier[pareto_idx[0]]
            can2 = self.pareto_frontier[pareto_idx[1]]
            #pick from frontier

            [crs1, crs2] = curr_pop.crossover(can1, can2)
            curr_pop.mutate(crs1)
            curr_pop.mutate(crs2)
            next_pop.candidates.append(crs1)
            next_pop.candidates.append(crs2)
        next_pop.ap_binary_dom()
        self.update_pareto(next_pop.pop_pareto)
        self.generations.append(next_pop)
        self.current_generation += 1
        return

    def statistics(self):
        curr_pop = self.generations[self.current_generation];
        best_fitness = sum(curr_pop.candidates[0].fitness)
        worst_fitness = sum(curr_pop.candidates[0].fitness)
        sum_fitness = 0
        for i in range(0, self.num_candidates):
            if(sum(curr_pop.candidates[i].fitness) < best_fitness):
                best_fitness = sum(curr_pop.candidates[i].fitness)
            if(sum(curr_pop.candidates[i].fitness) > worst_fitness):
                worst_fitness = sum(curr_pop.candidates[i].fitness)
            sum_fitness += sum(curr_pop.candidates[i].fitness)
        strStats = ""
        strStats += str(best_fitness) + ","
        strStats += str(worst_fitness) + ","
        strStats += str(sum_fitness / self.num_candidates)
        print strStats
        return

    def skdata(self):
        if self.current_generation % 100 != 99:
            return
        genStr = ""
        genStr += "gen" + str((self.current_generation+1)/100) + " "
        for pop in range(self.current_generation - 99, self.current_generation+1):
            curr_pop = self.generations[pop]
            for i in range(0, self.num_candidates):
                genStr += str(curr_pop.candidates[i].fitness[0]) + " "
        print genStr
        return

    def hvdata(self, hveCurr):
        hveCurr.add_data(self.generations[self.current_generation])
    
    def run(self):
        #self.initFile()
        self.randomize()
        #print 'Completed randomize'
        hveCurr = hve.HVE(self.num_candidates, self.num_generations)
        for i in range(0, self.num_generations):
            self.next()
            #print self.pareto_frontier
            self.hvdata(hveCurr)
            #self.writeToFile()
        hveCurr.pareto_last(self.pareto_frontier)
        return hveCurr
		
objs = [2,4,6,8]
decs = [10,20,40]
fitness_family = [dtlz.dtlz1, dtlz.dtlz3, dtlz.dtlz5, dtlz.dtlz7]
ff_names = ["dtlz1", "dtlz3", "dtlz5", "dtlz7"]

def init():
    for num_objs in objs:
        for num_decs in decs:
            for ff in ff_names:
                for i in range(0, num_objs):
                    f = open('data/{0}-{1}-{2}-f{3}.dat'.format(num_objs, num_decs, ff, i), 'w')
                    f.close()
                f = open('data/{0}-{1}-{2}-fsum.dat'.format(num_objs, num_decs, ff), 'w')
                f.close()

#def run_all():
#    for num_objs in objs:
#        for num_decs in decs:
#            for ff in fitness_family:
#                ga = GA(num_candidates, ff, num_objs, num_decs)
#                ga.randomize()
#                #ga.statistics()
#                for i in range(0, num_generations):
#                    ga.next()
#                    ga.statistics()
def main():
    ga = GA(fitness_family=dtlz.dtlz7, num_objs=2, num_decs=40, prob_mut=0.05, num_candidates=100, num_generations=1000)
    hve1 = ga.run()
    print "Hyper volume: " + str(hve1.hyper_vol)
    print "Spread: " + str(hve1.spread)

if __name__ == "__main__":
    cProfile.run('main()')
