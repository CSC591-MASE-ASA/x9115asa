from __future__ import division
from random import uniform
from random import randint
from random import random


xlower = [0,0,0,1,0,1,0]
xup = [0,10,10,5,6,5,10]
# EMIN = -369.242811007
# EMAX = 146.103629752

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


def equals(x1,x2):
    res = (len(x1) == len(x2))
    if res:
        for i in xrange(len(x1)):
            res = res and x1[i] == x2[i]
    return res
# def normalize(energy):
#     print "max-min=",(EMAX - EMIN)
#     print" e - emin" ,(energy - EMIN)
#     print energy > EMAX
#     enorm = (energy - EMIN)/(EMAX - EMIN)
#     return enorm

# x= [0, 2.0, 4.0, 3.4000000000000004, 3.756264391548214, 4.947047845201191, 9.819959509802576]
# print constraints(x)
# print osyczka2(x),EMIN,EMAX
# print normalize(osyczka2(x))
# print e,normalize(e,-369.242811007,146.103629752)

def baselinevals():
    minval = 1
    maxval = 0
    for i in xrange(200000):
        solution = randomassign()
        e = osyczka2(solution)
        if e < minval:
            minval = e
        if e > maxval:
            maxval = e

    # print "f1MAX = {0} \nf1MIN={1}\nf2MAX = {0} \nf2MIN={1}".format(f1max,f1min,f2max,f2min)
    print "MIN = {0}\nMAX = {1}".format(minval,maxval)


baselinevals()





# OUTPUT:
# Anishas-MacBook-Pro:5 anisha$ python basecalc.py
# MIN = -369.242811007
# MAX = 146.103629752
