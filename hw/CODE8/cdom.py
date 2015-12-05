import math
PI = math.pi
def loss1(i,x,y):
    return (x - y) if better(i) == lt else (y - x)

def expLoss(i,x,y,n):
    return math.exp( loss1(i,x,y) / n)

def loss(x1, y1):
    x,y    = objs(x1), objs(y1)
    n      = min(len(x), len(y)) #lengths should be equal
    losses = [ expLoss(i,xi,yi,n)
                 for i, (xi, yi)
                   in enumerate(zip(x,y)) ]
    # print losses
    return sum(losses) / n

def cdom(x, y):
   "x dominates y if it losses least"
   return x if loss(x,y) < loss(y,x) else y

def gt(x,y): return x > y
def lt(x,y): return x < y

def better(i):  return lt

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

def objs(can):
    return [f_one(can),f_two(can)]

# print cdom([4,13],[2,4])
