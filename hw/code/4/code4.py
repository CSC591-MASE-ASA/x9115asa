from __future__ import division
import random, math

class schaffer:
    min = 10**10
    max = -min
    lower, upper = -100000, 100000
    def normalize(self, value):
        #print self.min, self.max
        return (value - self.min)/(self.max - self.min)
    def denormalize(self, value):
        return (self.max - self.min)*value + self.min
    def gen_f1f2(self,val):
        return val**2, (val-2)**2
    
    def energy(self, value):
        f1,f2 = self.gen_f1f2(value)
        return self.normalize(f1+f2)
    
    def gen_x(self):
        return random.randrange(self.lower, self.upper)
    
    
    def schaffer_minmax(self):
        for i in range(100):
            x = self.gen_x()
            f1, f2 = self.gen_f1f2(x)
            sum = f1+f2
            if sum > self.max:
                self.max = sum
            if sum < self.min:
                self.min = sum
        return self.min, self.max
    def simmulated_annealing(self, kmax=1000, cooling = 0.6):
        k=0
        s = sb = self.gen_x()
        e = eb = self.energy(s)
        def P(old, new, t):
            val = (old-new)/t
            return math.exp(val) > random.random()
        while k < kmax:
            
            sn = self.gen_x()
            en = self.energy(sn)
            if en < eb:
                sb, eb = sn, en
                print '!',
            if en < e:
                s, e = sn, en
                print '+',
            elif P(e, en, (1-k/kmax)**cooling):
                s, e = sn, en
                print '?',
            print '.',
            k +=1
            if k%25==0:
                print '\n',
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