from __future__ import division
import math, random



#class sa:
#    def __init__(self):
#        self.name='place holder'
#        
#class mws:
#    def __init__(self):
#        self.name='place holder'


def sa(model):
    model.baseline()
    k=0
    kmax = 1000
    print 
    s = sb = model.get_decision()
    e = eb = model.energy(model.get_objectives(s))
    emax = -0.0000001
    print 's0 = ', s
    print 'e0 = ', e
    def P(old, new, t):
        val = (old-new)/t
        return math.exp(val)
    while k < kmax and e > emax:
        sn = model.neighbor(s)
        en = model.energy(model.get_objectives(sn))
        if k%25==0:
            print '\n',
            op = "%04d"%k+",%.2f"%en+", "
            print op,
        k+=1
        if en < eb:
            sb, eb = sn, en
            print '!',
        if en < e:
            s, e = sn, en
            print '+',
        elif P(e, en, k/kmax) < random.random():
            s, e = sn, en
            print '?',
        print '.',
        
        k +=1
    print
    return eb, sb