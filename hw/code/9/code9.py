import dtlz
import random
import math
import hve

def product(arr):
    mul = 1
    for i in range(0, len(arr)):
        mul *= arr[i]
    return mul

def GCD(a,b):
	a = abs(a)
	b = abs(b)
        while a:
                a, b = b%a, a
        return b

def GCD_List(list):
	return reduce(GCD, list)

def LCM_List(list):
    prod = product(list)
    lcm = prod / GCD_List(list)
    return lcm

class candidate:
    num_objs = 10

    def __init__(self, decs):
        self.decs = decs
        self.fitness = None
        self.dom_count = 0

    def calc_fitness(self, fitness_family):
        self.fitness = fitness_family(self.decs, self.num_objs, len(self.decs))
        return

    def __gt__(self, other):
        better = any([x < y for x,y in zip(self.fitness, other.fitness)])
        worse = any([x > y for x,y in zip(self.fitness, other.fitness)])
        return better and not worse

    def __repr__(self):
        return ",".join([str(x) for x in self.decs])


class population:
    num_candidates = 10;
    fitness_family = None
    prob_mut = 0.05
    num_decs = 2

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1):
        self.candidates = []
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family

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

    def mutate(self, candidate):
        for i in range(0, self.num_decs):
            if random.random() < self.prob_mut:
                candidate.decs[i] = random.random()
        return

    def __repr__(self):
        return ",".join([can.__repr__() for can in self.candidates])

    def ap_binary_dom(self):
        candidates = self.candidates
        n = self.num_candidates

        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    continue
                if candidates[i] > candidates[j]:
                    candidates[i].dom_count += 1

    def weighted_wheel(self):
        # weighted wheel technique of selection
        sumTemp = sum([x.dom_count for x in self.candidates])
        if sumTemp == 0:
            return self.candidates[random.randint(0, self.num_candidates-1)]
        rand = random.random()*sumTemp
        sumT = 0
        for i in range(0, self.num_candidates):
            sumT += self.candidates[i].dom_count
            if rand < sumT:
                return self.candidates[i]

class GA:
    fitness_family = None
    num_candidates = 100

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1, num_objs =10, num_decs = 2):
        self.generations = []
        self.current_generation = 0
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family
        candidate.num_objs = num_objs
        population.num_decs = num_decs
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
    
    def initFile(self):
        return
    
    def writeToFile(self):
        return
		

num_candidates = 100
num_generations = 1000
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

def run_all():
    for num_objs in objs:
        for num_decs in decs:
            for ff in fitness_family:
                ga = GA(num_candidates, ff, num_objs, num_decs)
                ga.randomize()
                #ga.statistics()
                for i in range(0, num_generations):
                    ga.next()
                    ga.statistics()

def run_one(num_objs, num_decs, fitness_family):
	ga = GA(num_candidates, fitness_family, num_objs, num_decs)
	ga.initFile()
	ga.randomize()
	hveCurr = hve.HVE()
	for i in range(0, num_generations):
		ga.next()
		ga.hvdata(hveCurr)
		ga.writeToFile()
	hveCurr.pareto_last()

run_one(2, 10, dtlz.dtlz1)
