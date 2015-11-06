# For DE and MWS and SA, code up the Type1,Type2, Type3 comparison operators and use them to:
#
# Find the final era computed by DE, MWS, SA (with early termination)
# Computer the loss numbers between era0 the final era
# Important implementation note: repeat the above with 20 different baseline populations. For each baseline, run DE,MWS,SA.
# Apply the above for DTLZ7 with 2 objectives 10 decisions.
#
# Using the statistical machinery discussed in class (Scott-Knott, a12, bootstrap) to decide in any of DE, MWS, SA is best for this model. TO collect data, 20 times, generate a baseline population and for each baseline, the run DE, MWS, SA from that baseline.

from __future__ import division
from random import uniform
from random import randint
from random import random
from sk import rdivDemo
import math


xlower = [0,0,0,0,0,0,0,0,0,0]
xup = [1,1,1,1,1,1,1,1,1,1]
PI = math.pi

def dtlz7(x):
    f1 = f_one(x)
    f2 = (1+g(x))*h(f1,g(x),2)
    return f1 + f2

def f_one(x):
    return x[0]

def g(x):
    res = sum(x)
    res = 1 + (9/len(x))*res
    return res

def h(f1,g,M):
    theeta = 3*PI*f1
    res = (f1/(1+g))*(1+math.sin(theeta))
    res = M - res
    return res

def type1(x,y):
    if dtlz7(x) < dtlz7(y):
        return x
    elif dtlz7(x) > dtlz7(y):
        return y
    else:
        return x

# Krall's Bstop method:
#
# For each objective do
# If any "improvement", give yourself five more lives
# Here, "improvement" could be
# Sort the values for that objective in era and era+1
# Run the fast a12 test to check for true difference
# Be mindful of objectives minimizing or maximizing.
# If no improvement on anything,
# Lives - 1

class o():
    def __init__(self,lst,m,eq,lt,n):
        self.l = lst
        self.m = m
        self.eq = eq
        self.lt = lt
        self.n = n

def type2(era1,era2):
    def a12(lst1,lst2):

        def loop(t,t1,t2):
            while t1.m < t1.n and t2.m < t2.n:
                h1 = t1.l[t1.m]
                h2 = t2.l[t2.m]
                h3 = t2.l[t2.m+1] if t2.m+1 < t2.n else None
                if h1 < h2:
                    t1.m  += 1; t1.lt += t2.n - t2.m
                elif h1 == h2:
                    if h3 and gt(h1,h3) < 0:
                        t1.lt += t2.n - t2.m  - 1
                        t1.m  += 1; t1.eq += 1; t2.eq += 1
                else:
                    t2,t1  = t1,t2
            return t.lt*1.0, t.eq*1.0
      #--------------------------
        lst1 = sorted(lst1,reverse=True)
        lst2 = sorted(lst2,reverse=True)
        n1   = len(lst1)
        n2   = len(lst2)
        t1   = o(l=lst1,m=0,eq=0,lt=0,n=n1)
        t2   = o(l=lst2,m=0,eq=0,lt=0,n=n2)
        lt,eq= loop(t1, t1, t2)
        return lt/(n1*n2) + eq/2/(n1*n2)

    a12_res = a12(era1,era2)
    if a12_res > 0.56:
        return 5
    else:
        return -1

def type3():
    eras = 5
    era_length = 100
    mw_maxtries = 500
    mw_maxchanges = 100
    mw_p = 0.5
    mw_threshold = 2
    mw_steps = 10
    era_collection = []

    for i in xrange(0,20):
        seed = randomassign()
        mw_sol, mw_era = max_walk_sat(eras,mw_maxtries,mw_maxchanges,mw_threshold,mw_p,mw_steps,era_length,seed)
        era_collection.append(["MaxWalkSat"+str(i+1)] + mw_era)
        sa_sol, sa_era = simmulated_annealing(1000,era_length,seed)
        era_collection.append(["SA"+str(i+1)] + sa_era)

    rdivDemo(era_collection)

def randomassign():
    x=[]
    for i in xrange(0,10):
        x.append(random())
    return x

def max_walk_sat(eras,maxtries,maxchanges,threshold,p,steps,era_length,seed):
    evals = 0
    sb = randomassign()
    total_evals = 0
    cprob = [0,0,0,0,0,0,0]
    # print "best solution \t current solution"
    this_era = []
    prev_era = []

    def change_random_c(x,c):
        x_new = x[:]
        # x_new[c] = uniform(xlower[c],xup[c])
        x_new[c] = random()
        res = type1(x,x_new)

    def change_c_to_maximize(x,c,steps):
        x_best = x[:]
        x_curr = x[:]
        dx = 1.0/float(steps)
        for i in xrange(0,steps):
            x_curr[c] = xlower[c] + dx*i
            if type1(x_curr,x_best) == x_curr:
                x_best = x_curr[:]

        # print "RET",x,x_best
        return type1(x,x_best)
    # while eras > 1:

    for i in xrange(0,maxtries):
        if i == 0:
            solution = seed
        else:
            solution = randomassign()
        # out = ""

        for j in xrange(0,maxchanges):
            stat = ""
            if dtlz7(solution) > threshold:
                return solution

            c = randint(0,9)
            cprob[c] += 1
            if p < random():
                solution = change_random_c(solution,c)

            else:
                solution = change_c_to_maximize(solution,c,steps)

            if type1(solution,sb) == solution:
                sb = solution[:]

        # print str(dtlz7(sb))+"\t" +str(dtlz7(solution)) + "\t\t"+out
        if i % era_length != 0:
            this_era.append(solution)
        else:
            if len(prev_era) > 0:
                eras = eras + type2(prev_era,this_era)
            prev_era = this_era[:]
            this_era = []
            if era < 1:
                break

    return sb,prev_era


def simmulated_annealing(kmax=1000,era_length,seed):
    # print
    def P(old, new, t):
        val = (old-new)/t
        return math.exp(val)

    def neighbor(x):
        xn = [:]
        index = randint(0,len(x)-1)
        xn[index] = random():
        return xn


    k=0
    s = sb = seed
    e = eb = dtlz7(s)
    emax = -1
    # print 's0 = ', s
    # print 'e0 = ', e
    eras = 5
    this_era = []
    prev_era = []
    # while k < kmax and e > emax and eras > 0:
    while True:
        sn = neighbor(s)
        en = dtlz7(sn)

        # if en < eb:
        if type1(en,eb) == en:
            sb, eb = sn, en

        # if en < e:
        if type1(en,e) == en:
            s, e = sn, en

        elif P(e, en, k/kmax) < random():
            s, e = sn, en

        k +=1
        if k % era_length:
            this_era.append(s)
        else:
            if len(prev_era) > 0:
                eras = eras + type2(prev_era,this_era)
            prev_era = this_era[:]
            this_era = []
            if k > kmax or eras < 1:
                break

    return sb, prev_era

def differential_evolution():
    return
