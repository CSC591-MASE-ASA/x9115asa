import dtlz
import random
import math
import hve
import sys
import sk

class candidate:
    num_objs = 10

    def __init__(self, decs):
        self.decs = decs
        self.fitness = None
        self.dom_count = 0

    # Calculate fitness of this candidate based on passed in fitness_family
    def calc_fitness(self, fitness_family):
        self.fitness = fitness_family(self.decs, self.num_objs, len(self.decs))
        return

    # Binary domination
    def __gt__(self, other):
        better = any([x < y for x,y in zip(self.fitness, other.fitness)])
        worse = any([x > y for x,y in zip(self.fitness, other.fitness)])
        return better and not worse

    def __repr__(self):
        return ",".join([str(x) for x in self.decs])

# Population is a collection of candidates and has the GA operations
class population:
    num_candidates = 10;
    fitness_family = None
    prob_mut = 0.05
    num_decs = 2

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1):
        self.candidates = []
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family

    # Initialize first generation
    def randomize(self):
        for i in range(self.num_candidates):
            can = candidate([])
            for j in range(self.num_decs):
                can.decs.append(random.random())
            can.calc_fitness(self.fitness_family)
            self.candidates.append(can)
        self.ap_binary_dom()

    # Cross over using random cross over point
    def crossover(self, candidate1, candidate2):
        crossover_point = random.randrange(0, self.num_decs)
        decs1 = []
        decs2 = []
        for i in range(0, crossover_point):
            decs1.append(candidate1.decs[i])
            decs2.append(candidate2.decs[i])
        for i in range(crossover_point, self.num_decs):
            decs1.append(candidate2.decs[i])
            decs2.append(candidate1.decs[i])
        can1 = candidate(decs1)
        can1.calc_fitness(self.fitness_family)
        can2 = candidate(decs2)
        can2.calc_fitness(self.fitness_family)
        return [can1, can2]

    def select(self):
        return self.weighted_wheel()

    # Mutate every bit with random probably
    def mutate(self, candidate):
        for i in range(0, self.num_decs):
            if random.random() < self.prob_mut:
                candidate.decs[i] = random.random()
        return

    def __repr__(self):
        return ",".join([can.__repr__() for can in self.candidates])

    # All pairs binary domination, dom_count is the number of other candidates a candidate dominates
    def ap_binary_dom(self):
        candidates = self.candidates
        n = self.num_candidates

        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    continue
                if candidates[i] > candidates[j]:
                    candidates[i].dom_count += 1

    # weighted wheel technique of selection based on dom_count
    def weighted_wheel(self):
        sumTemp = sum([x.dom_count for x in self.candidates])
        if sumTemp == 0:
            return self.candidates[random.randint(0, self.num_candidates-1)]
        rand = random.random()*sumTemp
        sumT = 0
        for i in range(0, self.num_candidates):
            sumT += self.candidates[i].dom_count
            if rand < sumT:
                return self.candidates[i]

# This class drives the GA algorithm
class GA:
    fitness_family = None
    num_candidates = 100

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1, num_objs =10, num_decs = 2, prob_mut=0.05):
        self.generations = []
        self.current_generation = 0
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family
        candidate.num_objs = num_objs
        population.num_decs = num_decs
        population.prob_mut = prob_mut
        return

    def randomize(self):
        gen1 = population(self.num_candidates, self.fitness_family)
        gen1.randomize()
        self.generations.append(gen1)
        return

    def next(self):
        curr_pop = self.generations[self.current_generation];
        next_pop = population(self.num_candidates, self.fitness_family)
        for i in range(0, self.num_candidates, 2):
            can1 = curr_pop.select()
            can2 = curr_pop.select()
            [crs1, crs2] = curr_pop.crossover(can1, can2)
            curr_pop.mutate(crs1)
            curr_pop.mutate(crs2)
            next_pop.candidates.append(crs1)
            next_pop.candidates.append(crs2)
        next_pop.ap_binary_dom()
        self.generations.append(next_pop)
        self.current_generation += 1
        return

    def hvdata(self, hveCurr):
        hveCurr.add_data(self.generations[self.current_generation])
    
    def calc_a12(self):
        if self.current_generation % 100 != 99 or self.current_generation < 199:
            return 0
        gen1 = []
        gen2 = []
        for i in range(self.current_generation-199, self.current_generation-99):
            gen1 += self.generations[i].candidates
        for i in range(self.current_generation-99, self.current_generation+1):
            gen2 += self.generations[i].candidates
        sum1 = [sum(c.fitness) for c in gen1]
        sum2 = [sum(c.fitness) for c in gen2]
        a12 = sk.a12(sum1, sum2)
        return 1 if a12 > 0.56 else 0
    
    def run(self, num_generations=1000):
        self.randomize()
        hveCurr = hve.HVE()
        num_lives = 5
        for i in range(0, num_generations):
            self.next()
            self.hvdata(hveCurr)
            num_lives -= self.calc_a12()
            if num_lives == 0:
                break
        return hveCurr.pareto_last()
		
objs = [2,4,6,8]
decs = [10,20,40]
fitness_family = [dtlz.dtlz1, dtlz.dtlz3, dtlz.dtlz5, dtlz.dtlz7]
ff_names = ["dtlz1", "dtlz3", "dtlz5", "dtlz7"]

def run_all():
    for num_objs in objs:
        for num_decs in decs:
            for f in range(0, len(fitness_family)):
                ff = fitness_family[f]
                fname = ff_names[f]
                sys.stderr.write("{0}-{1}-{2}\n".format(fname, num_objs, num_decs))
                filedes = open("data/ga-{0}-{1}-{2}.txt".format(fname, num_objs, num_decs), 'w')
                run_one_n_times(num_candidates=100, fitness_family=ff, num_objs=num_objs, num_decs=num_decs, num_generations=1000, filedes=filedes)
                filedes.close()
                    
def run_one_n_times(num_candidates, fitness_family, num_objs, num_decs, num_generations, filedes, num_runs=20):
    results = []
    for i in range(0, num_runs):
        sys.stderr.write("Run " + str(i) + "\n")
        ga = GA(num_candidates, fitness_family, num_objs, num_decs)
        hve_res = ga.run(num_generations)
        results.append(hve_res)
    
    hyper_vols = [res.hyper_vol for res in results]
    filedes.write("Hypervolume: " + str(hyper_vols) + "\n")
    filedes.write("Spread: " + str([str(res.spread) for res in results]) + "\n")
    
    avg = sum(hyper_vols) / len(hyper_vols)
    hmax = max(hyper_vols)
    hmin = min(hyper_vols)
    dev = max([hmax-avg,avg-hmin])
    filedes.write("Hypervolume Deviation: " + str(avg) + "+-" + str(dev) + "\n")

### Scripts

### Run one instance of GA 20 times. Results are collected in the file ga.txt
#filedes = open("ga.txt", 'w')
#run_one_n_times(num_candidates=25, fitness_family=dtlz.dtlz1, num_objs=2, num_decs=10, num_generations=150, filedes=filedes, num_runs=20)

#### Run one instance of GA
#ga = GA(num_candidates=100, fitness_family=dtlz.dtlz1, num_objs=2, num_decs=10, prob_mut=0.05)
#hve1 = ga.run(num_generations=1000)
#print "Hyper volume: " + str(hve1.hyper_vol)
#print "Spread: " + str(hve1.spread)

### Run all instances of GA 20 times (warning: this takes hours)
#run_all()