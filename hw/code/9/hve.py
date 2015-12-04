import random

class HVE:
    def __init__(self):
        self.generations = []

    def add_data(self, generation):
        self.generations.append(generation)
    
    def pareto_last(self):
        frontier = self.generations[len(self.generations)-1]
        fron_cans = frontier.candidates[:]
        num_cans = 100000
        for i in range(0, num_cans):
            rand_num1 = random.randint(0, len(frontier.candidates)-1)
            ran_fron = fron_cans[rand_num1]

            # Sel random from rest
            ran_gen = self.generations[random.randint(0, len(self.generations)-2)]
            rand_num2 = random.randint(0, len(ran_gen.candidates)-1)
            ran_can = ran_gen.candidates[rand_num2]

            if ran_fron > ran_can:
                continue
            elif ran_can > ran_fron:
                fron_cans[rand_num1] = ran_can
                ran_gen.candidates[rand_num2] = ran_fron
            else:
                fron_cans.append(ran_can)
        
        # Trying to clean up pareto and calculating spread
        spread_max = fron_cans[0].fitness[:]
        spread_min = fron_cans[0].fitness[:]
        for i in range(0, len(fron_cans)):
            #Getting min,max values for every objective
            for k in range(0, len(fron_cans[i].fitness)):
                if spread_min[k] > fron_cans[i].fitness[k]:
                    spread_min[k] = fron_cans[i].fitness[k]
                if spread_max[k] < fron_cans[i].fitness[k]:
                    spread_max[k] = fron_cans[i].fitness[k]
            
            # Seeing if any candidate in the frontier is bin dom by every other in the frontier, if yes then can remove it
            flag = True
            for j in range(0, len(fron_cans)):
                if i == j:
                    continue
                if i >= len(fron_cans) or j >= len(fron_cans):
                    break

                if fron_cans[i] > fron_cans[j]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                del fron_cans[j]
        
        print "Hyper volume: " + str((num_cans-len(fron_cans))/float(num_cans))
        print "Spread: " + str([x-y for x,y in zip(spread_max, spread_min)])
                    