import random

class Result:
    def __init__(self, hyper_vol, spread):
        self.hyper_vol = hyper_vol
        self.spread = spread

class HVE:
    def __init__(self):
        self.generations = []
        self.hyper_vol=0
        self.spread=[]

    def add_data(self, generation):
        self.generations.append(generation)
    
    def pareto_last(self, pf):
        frontier = self.generations[len(self.generations)-1]
        fron_cans = pf
        num_cans = 100000
        #for i in range(0, num_cans):
        #    rand_num1 = random.randint(0, len(frontier.candidates)-1)
        #    ran_fron = fron_cans[rand_num1]
#
        #    # Sel random from rest
        #    ran_gen = self.generations[random.randint(0, len(self.generations)-2)]
        #    rand_num2 = random.randint(0, len(ran_gen.candidates)-1)
        #    ran_can = ran_gen.candidates[rand_num2]
#
        #    if ran_fron > ran_can:
        #        continue
        #    elif ran_can > ran_fron:
        #        fron_cans[rand_num1] = ran_can
        #        ran_gen.candidates[rand_num2] = ran_fron
        #    else:
        #        fron_cans.append(ran_can)
        #
        # Trying to clean up pareto
        #for i in range(0, len(fron_cans)):
        #    # Seeing if any candidate in the frontier is bin dom by every other in the frontier, if yes then can remove it
        #    flag = True
        #    for j in range(0, len(fron_cans)):
        #        if i == j:
        #            continue
        #        if i >= len(fron_cans) or j >= len(fron_cans):
        #            break
#
        #        if fron_cans[i] > fron_cans[j]:
        #            flag = True
        #        else:
        #            flag = False
        #            break
        #    if flag:
        #        del fron_cans[j]
        #
        # Calculating spread
        spread = []
        for i in range(0, len(fron_cans[0].fitness)):
            fsorted = sorted(fron_cans, lambda x,y: x.fitness[i] < y.fitness[i])
            p25 = fsorted[len(fsorted)/4]
            p75 = fsorted[3*len(fsorted)/4]
            spread.append(abs(p75.fitness[i]-p25.fitness[i]))
        self.spread=spread
        self.hyper_vol = (num_cans-len(fron_cans))/float(num_cans)
        res = Result(self.hyper_vol, self.spread)
        return res