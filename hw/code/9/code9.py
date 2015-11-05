import dtlz
import random

num_objs = 2
num_decs = 10

class candidate:
    fitness = 0
    decs = []
    def __init__(self, decs):
        self.decs = decs

    def calc_fitness(self, fitness_family):
        f = fitness_family(self.decs, num_objs, len(self.decs))
        self.fitness = sum(f)
        return

class population:
    candidates = []
    num_candidates = 10;
    fitness_family = None

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1):
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family

    def randomize(self):
        for i in range(self.num_candidates):
            can = candidate([])
            for j in range(num_decs):
                if random.random() > 0.5:
                    can.decs.append(1)
                else:
                    can.decs.append(0)
            can.calc_fitness(self.fitness_family)
            self.candidates.append(can)

    def crossover(self, candidate1, candidate2):
        return
    def select(self):
        return
    def mutate(self, candidate, probability):
        return

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
        return

    def next():
        return

    def statistics():
        return

ga = GA(20, dtlz.dtlz1)
ga.randomize()
