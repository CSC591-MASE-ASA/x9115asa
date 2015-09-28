from __future__ import division
import random, math

class schaffer:
    min = 10.01**5
    max = -min
    lower, upper = -10**5, 10**5
    def normalize(self, value):
        #print self.min, self.max
        return (value - self.min)/(self.max - self.min)
    #def denormalize(self, value):
    #    return (self.max - self.min)*value + self.min
    def gen_f1f2(self,val):
        return val**2, (val-2)**2
    
    def energy(self, value):
        f1,f2 = self.gen_f1f2(value)
        return self.normalize(f1+f2)
    
    def neighbor(self, s):
        nb_range = int((max(math.fabs(s-self.lower), math.fabs(s-self.upper)))/4)
        return random.randrange(int(s-nb_range), int(s+nb_range))
    
    def schaffer_minmax(self):
        for i in range(1000):
            x =  random.randrange(self.lower, self.upper)
            f1, f2 = self.gen_f1f2(x)
            sum = f1+f2
            if sum > self.max:
                self.max = sum
            if sum < self.min:
                self.min = sum
        return self.min, self.max
    def simmulated_annealing(self, kmax=1000, cooling = 0.6):
        k=0
        print 
        s = sb = random.randrange(self.lower, self.upper)
        e = eb = self.energy(s)
        emax = -2
        print 's0 = ', s
        print 'e0 = ', e
        def P(old, new, t):
            val = (old-new)/t
            return math.exp(val)
        while k < kmax and e > emax:
            sn = self.neighbor(s)
            en = self.energy(sn)
            if en < eb:
                sb, eb = sn, en
                print '!',
            if en < e:
                s, e = sn, en
                print '+',
            elif P(e, en, (1-k/kmax)) > random.random():
                s, e = sn, en
                print '?',
            print '.',
            if k%25==0:
                print '\n',
                op = "%04d"%k+",%.2f"%en+", "
                print op,
            k +=1
        print
        return eb, sb


def main():
    schaff = schaffer()
    minmax = schaff.schaffer_minmax()
    eb, sb =schaff.simmulated_annealing(kmax = 1000, cooling = 1)
    print 'kmax = 1000'
    print 'cooling = 1'
    print '(min, max) is ', minmax
    print 'eb = ', eb
    print 'sb = ', sb
                
if __name__ == '__main__':
    main()