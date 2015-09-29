from __future__ import division
from random import uniform
from random import randint
from random import random


xlower = [0,0,0,1,0,1,0]
xup = [0,10,10,5,6,5,10]


def isok(g,x):
    for i in xrange(1,7):
        # print g[i] < 0
        if g[i] < 0:
            # print "FAIL!!",i,g[i],x
            return False
    return True


def constraints(x):
    g=[10,0,0,0,0,0,0]
    g[1]=x[1]+x[2]-2
    g[2]=6-x[1]-x[2]
    g[3]=2-x[2]+x[1]
    g[4]=2-x[1]+3*x[2]
    g[5]=4-x[4]-(x[3]-3)**2
    g[6]=(x[5]-3)**3+x[6]-4
    return isok(g,x)

def osyczka2(x):
    f1 = 25*(x[1]-2)**2 + (x[2]-2)**2 + (x[3]-1)**2 * (x[4]-4)**2 + (x[5]-1)**2
    f1 = -1 * f1
    f2 = 0
    for i in xrange(1,7):
        f2 += x[i]**2
    return f1 + f2

def randomassign():
    x = [0,0,0,0,0,0,0]
    while True:
        for i in xrange(1,7):
            x[i] = uniform(xlower[i],xup[i])
        if constraints(x):
            return x

def change_random_c(x,c):
    x_old = osyczka2(x)
    timer = 1000
    no_evals = 0
    while timer > 0:
        x[c] = uniform(xlower[c],xup[c])
        no_evals += 1
        if constraints(x):
            break
        timer-=timer

    x_osyczka2 = osyczka2(x)
    if x_osyczka2 < x_old:
        return "?", no_evals, x
    elif x_osyczka2 > x_old:
        return "+", no_evals, x
    else:
        return ".", no_evals, x


# Given min to max values for every value, try steps of (max - min)/steps for, say, steps=10
def change_c_to_maximize(x,c,steps):
    x_best = x
    x_curr = x
    dx = (xup[c] - xlower[c])/float(steps)
    no_evals = 0
    for i in xrange(0,steps):
        no_evals += 1
        x_curr[c] = xlower[c] + dx*i
        if constraints(x_curr) and osyczka2(x_curr) > osyczka2(x_best):
            x_best = x_curr

    # print "RET",x,x_best
    if osyczka2(x) == osyczka2(x_best):
        return ".", no_evals, x
    else:
        return "+", no_evals, x_best

def equals(x1,x2):
    res = (len(x1) == len(x2))
    if res:
        for i in xrange(len(x1)):
            res = res and x1[i] == x2[i]
    return res


# Pseudocode :
# FOR i = 1 to max-tries DO
#   solution = random assignment
#   FOR j =1 to max-changes DO
#     IF  score(solution) > threshold
#         THEN  RETURN solution
#     FI
#     c = random part of solution
#     IF    p < random()
#     THEN  change a random setting in c
#     ELSE  change setting in c that maximizes score(solution)
#     FI
# RETURN failure, best solution found
def max_walk_sat(maxtries,maxchanges,threshold,p,steps):
    evals = 0
    sb = randomassign()
    total_evals = 0
    print "best solution \t current solution"
    for i in xrange(0,maxtries):
        solution = randomassign()
        out = ""

        for j in xrange(0,maxchanges):
            stat = ""
            if osyczka2(solution) > threshold:
                return solution

            c = randint(1,6)
            if p < random():
                stat, evals, solution = change_random_c(solution,c)

            else:
                stat, evals, solution = change_c_to_maximize(solution,c,steps)

            if osyczka2(solution) > osyczka2(sb):
                stat = "!"
                sb = solution[:]
            out = out + stat
            total_evals += evals

        print str(osyczka2(sb))+"\t" +str(osyczka2(solution)) + "\t\t"+out

    print "Parameters used maxtries={0}\t maxchanges={1}\t p={2}\t threshold={3}\t steps={4}".format(maxtries,maxchanges,p,threshold,steps)
    print "Total evaluations: {0}".format(total_evals)
    print "Final solution: {0} \nFinal energy : {1}".format(sb[1:],osyczka2(sb))

maxtries=500
maxchanges=50
p=0.5
threshold=1000000
steps=10

max_walk_sat(maxtries,maxchanges,threshold,p,steps)
