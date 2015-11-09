import dtlz
import random
import math

num_objs = 2
num_decs = 10

class candidate:
    def __init__(self, decs):
        self.decs = decs
        self.fitness = None

    def calc_fitness(self, fitness_family):
        self.fitness = fitness_family(self.decs, num_objs, len(self.decs))
        return

    def __repr__(self):
        return "".join([str(x) for x in self.decs])


class population:
    num_candidates = 10;
    fitness_family = None
    prob_mut = 0.05

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1):
        self.candidates = []
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family

    def randomize(self):
        for i in range(self.num_candidates):
            can = candidate([])
            for j in range(num_decs):
                if random.random() >= 0.5:
                    can.decs.append(1)
                else:
                    can.decs.append(0)
            can.calc_fitness(self.fitness_family)
            self.candidates.append(can)

    def crossover(self, candidate1, candidate2):
        crossover_point = random.randrange(0, num_decs)
        decs1 = []
        decs2 = []
        for i in range(0, crossover_point):
            decs1.append(candidate1.decs[i])
            decs2.append(candidate2.decs[i])
        for i in range(crossover_point, num_decs):
            decs1.append(candidate2.decs[i])
            decs2.append(candidate1.decs[i])
        can1 = candidate(decs1)
        can1.calc_fitness(self.fitness_family)
        can2 = candidate(decs2)
        can2.calc_fitness(self.fitness_family)
        return [can1, can2]

    def select(self):
        return self.candidates[random.randrange(0, self.num_candidates)]

    def mutate(self, candidate):
        for i in range(0, num_decs):
            if random.random() < self.prob_mut:
                candidate.decs[i] = candidate.decs[i] ^ 1
        return

    def __repr__(self):
        return ",".join([can.__repr__() for can in self.candidates])

class GA:
    generations = []
    fitness_family = None
    num_candidates = 10
    current_generation = 0

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1):
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family
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
        self.generations.append(next_pop);
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
        print [sum(can.fitness) for can in curr_pop.candidates]
        print "Best fitness: " + str(best_fitness)
        print "Worst fitness: " + str(worst_fitness)
        print "Avg fitness: " + str(sum_fitness / self.num_candidates)
        return

ga = GA(10, dtlz.dtlz1)
ga.randomize()
ga.statistics()
ga.next()
