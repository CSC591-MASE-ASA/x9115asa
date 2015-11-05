import dtlz
fitness_family = None

class candidate:
    fitness = 0
    decs = []
    def __init__(self, decs):
        self.decs = decs
        calc_fitness()

    def calc_fitness():
        return

class population:
    candidates = []
    num_candidates = 10;
    fitness_family = None

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1):
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family

    def randomize(self):
        return

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

    def randomize():
        return

    def next():
        return

    def statistics():
        return

ga = GA(dtlz.dtlz1)
