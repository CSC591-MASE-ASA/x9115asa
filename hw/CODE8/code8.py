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
from sk import a12
from sk import different
import math


xlower = [0,0,0,0,0,0,0,0,0,0]
xup = [1,1,1,1,1,1,1,1,1,1]
PI = math.pi
eras = 5
era_length = 100
mw_maxtries = 500
mw_maxchanges = 100
mw_p = 0.5
mw_threshold = 2
mw_steps = 10
era_collection = []
de_cr = 0.4
de_f  = 0.5
de_npExpand = 10

def dtlz7(x):
    f1 = f_one(x)
    f2 = (1+g(x))*h(f1,g(x),2)
    return f1 + f2
    # return f2

def f_one(x):
    return x[0]

def f_two(x):
    f1 = f_one(x)
    f2 = (1+g(x))*h(f1,g(x),2)
    return f2

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
    # minimized = False
    if (f_one(x) < f_one(y)) and (f_two(x) < f_two(y)):
        return x
    else:
        return y


def calc_obj1(sol):
    res = [f_one(x) for x in sol]
    return res

def calc_obj2(sol):
    res = [f_two(x) for x in sol]
    return res

def median(lst):
    return sum(lst)/len(lst)
    # lst = sorted(lst)
    # if len(lst) < 1:
    #     return None
    # if len(lst) %2 == 1:
    #     return lst[int((len(lst)+1)/2)-1]
    # else:
    #     return float(sum(lst[int(len(lst)/2)-1:int(len(lst)/2)+1]))/2.0




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

def cal_median_for_era(era):
    res = [dtlz7(x) for x in era]
    return median(res)

def type2(era1,era2):
    a12_o1 = different(calc_obj1(era1),calc_obj1(era2))
    a12_o2 = different(calc_obj2(era1),calc_obj2(era2))
    if a12_o1 or a12_o2:
        return 5
    else:
        # print a12_o1,a12_o2
        return -1

def type3():
    eras = 5
    era_length = 5
    mw_maxtries = 500
    mw_maxchanges = 100
    mw_p = 0.5
    mw_threshold = 2
    mw_steps = 10
    de_cr = 0.4
    de_f  = 0.5
    for i in xrange(2):
        seed = randomassign()
        mw_sol, mw_era = max_walk_sat(mw_maxtries,mw_maxchanges,999,mw_p,mw_steps,seed)
        label = "MWS"+str(i+1)
        res = [dtlz7(x) for x in mw_era]
        res.insert(0,label)
        era_collection.append(res)

        sa_sol, sa_era = simmulated_annealing(1000,era_length,seed,eras)
        label = "SA"+str(i+1)
        res = [dtlz7(x) for x in sa_era]
        res.insert(0,label)
        era_collection.append(res)
        de_sol, de_era = differential_evolution(era_length, seed, de_cr, de_f, 100,eras)
        label = "DE"+str(i+1)
        res = [dtlz7(x) for x in de_era]
        res.insert(0,label)
        era_collection.append(res)


    # print era_collection
    print rdivDemo(era_collection)


def randomassign():
    x=[]
    for i in xrange(0,10):
        x.append(random())
    return x

def max_walk_sat(maxtries,maxchanges,threshold,p,steps,seed):
    evals = 0
    sb = randomassign()
    total_evals = 0
    cprob = [0,0,0,0,0,0,0]
    this_era = []
    prev_era = []

    eras = 5
    era_length = 25
    def change_random_c(x,c):
        x_new = x[:]
        x_new[c] = random()
        res = type1(x,x_new)
        return res

    def change_c_to_minimize(x,c,steps):
        x_best = x[:]
        x_curr = x[:]
        dx = 1.0/float(steps)
        for i in xrange(0,steps):
            x_curr[c] = xup[c] - dx*i
            if type1(x_curr,x_best) == x_curr:
                x_best = x_curr[:]
        res = type1(x,x_best)
        return res

    sb = seed[:]
    solution = seed[:]
    # era = eras
    print_sol_sb = []
    print_sol = []
    op = ""
    all_eras = []
    all_best = []
    for i in xrange(0,maxtries):
        # print "i",i
        if i != 0:
            solution = randomassign()

        for j in xrange(0,maxchanges):
            if dtlz7(solution) > threshold:
                return solution

            c = randint(0,9)
            # cprob[c] += 1
            if p < random():
                solution = change_random_c(solution,c)

            else:
                solution = change_c_to_minimize(solution,c,steps)

        if type1(solution,sb) == solution :
            sb = solution[:]

        # op = op + str(i+1)+","+str(dtlz7(sb)) +","+str(dtlz7(solution)) + "\n"

        if i==0 or i % era_length != 0:
            # print i,era_length
            this_era.append(solution)
            # print "appending"
        else:
            if len(prev_era) > 0:
                print "eras",eras
                eras = eras + type2(prev_era,this_era)
            prev_era = this_era[:]
            this_era = []
            if eras < 1:
                print "eras limit",eras
                break
    # for i in xrange(len(all_eras)):
    #     op = op + str(i+1)+","+str(all_eras[i])++","+str(all_best[i])+"\n"
    #
    # print op
    # print all_best
    return sb,prev_era


def simmulated_annealing(kmax,era_length,seed,eras):

    def P(en, e, t):
        val = (e-en)/t
        try:
            return math.exp(val)
        except:
            # print "zero"
            return 0

    def neighbor(x):
        xn = x[:]
        # index = randint(0,len(x)-1)
        # xn[index] = random()
        p = 0.25
        for n in xrange(len(x)):
            val = x[n]
            if p > random():
                val = random()
            xn[n] = val
        return xn

    k=0
    sb = seed[:]
    s = sb[:]
    e = dtlz7(s)
    eb = dtlz7(s)
    emax = -1
    this_era = []
    prev_era = []
    all_eras =[]
    all_best = []
    op = ""
    while True:
        k +=1
        sn = neighbor(s)
        en = dtlz7(sn)

        if type1(sn,sb) == sn:
            sb = sn[:]
            eb =  en


        if type1(sn,s) == sn:
            s = sn[:]
            e = en

        elif P(en, e, k/kmax) < random():
            s = sn[:]
            e = en

        if k == 0 or k % era_length != 0:
            this_era.append(s)
        else:
            if len(prev_era) > 0:
                # print "eras_prev",eras
                eras = eras + type2(prev_era,this_era)
                # print "eras_curr",eras
            prev_era = this_era[:]
            this_era = []
            if k > kmax or eras < 1:
                print k,kmax,eras<1
                print "eras",eras
                break

    for i in xrange(len(all_eras)):
        op = op + str(i+1)+","+str(all_eras[i])+","+str(all_best[i])+"\n"

    print op
    return sb, prev_era

def differential_evolution(era_length, seed, cr, f, k_max,eras):
    np = era_length
    k = 0
    def xPlusFyz(x,y,z):
        sn=[]
        def smear((x1, y1, z1)):
            x1 = x1 if cr <= random() else x1 + f*(y1-z1)
            return x1
        for i in xrange(0,len(x)):
            sn = [smear(these) for these in zip(x,y,z)]
        return sn

    def create_frontier(seed):
        frontier = []
        frontier.append(seed)
        for i in xrange(1, np):
            frontier.append(randomassign())
        return frontier

    def generate_items(lst, avoid=None):
        def unique_item():
            x = avoid
            while id(x) in seen:
              x = lst[  int(uniform(0,len(lst))) ]
            seen.append( id(x) )
            return x

        assert len(lst) > 4
        avoid = avoid or lst[0]
        seen  = [ id(avoid) ]
        return unique_item(), unique_item(), unique_item()

    def era_energy(final_frontier):
        res = []
        for i in xrange(0,len(final_frontier)):
            res.append(dtlz7(final_frontier[i]))
        return res

    frontier = create_frontier(seed)
    # print "----------------------initial frontier-------------------------"
    # # print frontier
    # print "---------------------------------------------------------------"
    s = seed[:]
    sb = seed[:]
    e = eb = dtlz7(seed)

    all_eras = []

    prev_era = []
    this_era = []
    while True:
        for i,candidate in enumerate(frontier):
            x, y, z = generate_items(frontier)
            sn = xPlusFyz(x,y,z)
            en = dtlz7(sn)
            if type1(sb,sn) == sn:
                sb = sn[:]
                eb = en
            if type1(candidate,sn) == sn:
                frontier[i] = sn
            k = k + 1
        this_era = frontier[:]
        if len(prev_era) > 0:
            # print "eras:",eras
            eras = eras + type2(prev_era,this_era)
        prev_era = this_era[:]
        this_era = []

        if k> k_max or eras < 1:
            print "k",k
            print "eras",eras
            break
        # print "-------------ERA:"+ str(k/era_length) + "--------------------"
        # print prev_era
        # print "------------------------------------------------------------------"

    return sb, prev_era


def test():
    x = randomassign()
    maxchanges=25
    p=0.5
    era_length = 25
    eras = 5
    maxtries=10000
    kmax =10000
    cr = de_cr
    f = de_f
    # best,era = simmulated_annealing(kmax,era_length,x)
    # print best,dtlz7(best)

    # print best,era
    # # best,era = differential_evolution(era_length, x, cr, f, kmax,eras)
    # # print "best",dtlz7(best)
    # best,era = max_walk_sat(eras,maxtries,maxchanges,999,p,10,era_length,x)
    #
    # print "BEST:",best
    # print "BEST energy",dtlz7(best)
    # # print "last_era:",era
    # print a12([1,9,2],[4,5,6])
    type3()

test()
