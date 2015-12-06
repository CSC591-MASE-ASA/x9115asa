## Code 8

### Abstract
In order to derive the optimal solution, one can use different optimizers to solve the optimization problem. However how does one choose one optimizer over another given that each optimizer has its own pros and cons. This report presents a comparison between the performance of three optimizers i.e. Differential Evolution, Simulated annealing and Max-Walk Sat. We use the statistical machinery like t-Knott, a12, bootstrap to decide which of DE, MWS, SA is best for the model. The model chosen for this experiment is the DTLZ7 model.

### Background
#### Differential Evolution
Differential evolution (DE) is a method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. Such methods are commonly known as meta heuristics as they make few or no assumptions about the problem being optimized and can search very large spaces of candidate solutions. However, meta heuristics such as DE do not guarantee an optimal solution is ever found.

DE is used for multidimensional real-valued functions but does not use the gradient of the problem being optimized, which means DE does not require for the optimization problem to be differentiable as is required by classic optimization methods such as gradient descent and quasi-newton methods. DE can therefore also be used on optimization problems that are not even continuous, are noisy, change over time, etc.

DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones according to its simple formulae, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. In this way the optimization problem is treated as a black box that merely provides a measure of quality given a candidate solution and the gradient is therefore not needed.

#### Simulated annealing
Simulated annealing is so named because of its analogy to the process of physical annealing with solids, in which a crystalline solid is heated and then allowed to cool very slowly until it achieves its most regular possible crystal lattice configuration (i.e., its minimum lattice energy state), and thus is free of crystal defects.
If the cooling schedule is sufficiently slow, the final configuration results in a solid with such superior structural integrity.
Simulated annealing establishes the connection between this type of thermo- dynamic behavior and the search for global minima for a discrete optimization problem.
Furthermore, it provides an algorithmic means for exploiting such a connection

#### Max-walkSat
MaxWalkSat is a non-parametric stochastic method for sampling the landscape of the local region. Historically speaking, MaxWalkSat was a very impactful algorithm. But, at least here, the real purpose of discussing MaxWalkSat is to introduce the idea of landscapes. It will be argued that more important than the algorithms is the shape of the space they search. Since this shape can change, it is not possible to prove the adequacy of these meta-heuristics unless you first characterize the space they are trying to explore.

### Implementation and results
In this experiment, we evaluate three optimizers:
1. Simulated annealing
2. Max Walk Sat
3. Differential Evolution

In order to do this we use three comparators:

##### Type 1 comparator:
This comparator is used to compare two candidate solutions. This comparator is used when the optimizers are comparing pairs of candidates as each of the optimizers generate solutions
In order to do this we have used continuous domination:
In this method differences between Xi and Yi are registered on an exponential scale, so any differences SHOUT louder.

```python
def loss1(i,x,y):
    return (x - y) if better(i) == lt else (y - x)

def expLoss(i,x,y,n):
    return math.exp(loss1(i,x,y) / n)

def loss(x1, y1):
    x,y    = objs(x1), objs(y1)
    n      = min(len(x), len(y)) #lengths should be equal
    losses = [ expLoss(i,xi,yi,n)
                 for i, (xi, yi)
                   in enumerate(zip(x,y))]
    return sum(losses) / n

def cdom(x, y):
   "x dominates y if it losses least"
   return x if loss(x,y) < loss(y,x) else y
```

We used continuous domination over binary domination since binary domination did not give good results for models with large number of objectives.

The code snippet for the type 1 operator is below:
```python
def type1(x,y):
    return cdom(x,y)
```
##### Type 2 comparator
This operator is used to cause early termination. Early termination takes place when the optimizer does not generate eras of solutions that are better than the previous era.

The two consecutive eras are compared using Vargha and Delaney's A12 statistic. According to Vargha and Delaney, a small difference between two populations is 56% or less. Thus 0.56 was used as a cutoff.

Krall's Bstop method was incorporated to come up with the number of eras that should be added or subtracted.

Code snippet for the type 2 operator is:
```python
def type2(era1,era2):
    if a12_o1 >=0.56 or a12_o2>0.56:
        return 5
    else:
        return -1
```

The number of times early termination was achieved by the optimizers is as below:

| Optimizer | Number of  early terminations  |
|-----------|--------------------------------|
| DE        | 13                             |
| MWS       | 7                              |
| SA        | 2                              |



##### Type 3 comparator
This comparator is used to compare the final era generated by the optimizers.
The performance statistic used in this case is the aggregate of the objectives.
20 repeats were performed

Output:
```unix
rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 ,          DE6 ,    10.61  ,  2.02 (         -*--  |              ), 10.03,  10.61,  12.05
   1 ,          DE2 ,    10.73  ,  1.43 (        --*-   |              ), 9.91,  10.74,  11.34
   2 ,         DE19 ,    11.35  ,  1.50 (           -*- |              ), 10.89,  11.35,  12.39
   2 ,         DE13 ,    11.52  ,  0.78 (           -*  |              ), 11.18,  11.52,  11.96
   2 ,          DE9 ,    11.79  ,  2.36 (          ---*-|              ), 10.56,  11.81,  12.92
   3 ,        MWS11 ,    12.35  ,  2.22 (            --*|--            ), 11.59,  12.35,  13.82
   3 ,         MWS5 ,    12.36  ,  2.11 (            --*|-             ), 11.42,  12.36,  13.53
   3 ,        MWS19 ,    12.43  ,  2.60 (            --*|--            ), 11.41,  12.43,  14.01
   3 ,        MWS15 ,    12.44  ,  2.33 (            --*|--            ), 11.52,  12.44,  13.85
   3 ,         DE14 ,    12.52  ,  1.36 (              -*-             ), 12.08,  12.54,  13.45
   3 ,        MWS10 ,    12.57  ,  2.42 (            ---*-             ), 11.29,  12.57,  13.71
   3 ,         MWS9 ,    12.61  ,  2.41 (            ---*--            ), 11.41,  12.61,  13.82
   3 ,         MWS4 ,    12.61  ,  2.34 (            ---*-             ), 11.22,  12.61,  13.56
   3 ,        MWS18 ,    12.62  ,  2.19 (            ---*--            ), 11.62,  12.62,  13.81
   3 ,         MWS2 ,    12.67  ,  2.10 (            ---*-             ), 11.60,  12.67,  13.70
   3 ,         MWS6 ,    12.71  ,  1.88 (             --*-             ), 11.74,  12.71,  13.62
   3 ,        MWS14 ,    12.74  ,  1.85 (             --*-             ), 11.71,  12.74,  13.56
   3 ,          DE4 ,    12.74  ,  0.82 (              -*              ), 12.31,  12.75,  13.13
   3 ,        MWS16 ,    12.77  ,  2.80 (            ---*---           ), 11.38,  12.77,  14.18
   3 ,         MWS7 ,    12.78  ,  2.26 (             --*--            ), 11.65,  12.78,  13.91
   3 ,         DE12 ,    12.78  ,  1.20 (              -*-             ), 12.22,  12.79,  13.42
   3 ,        MWS12 ,    12.80  ,  2.24 (            ---*--            ), 11.56,  12.80,  13.81
   3 ,        MWS13 ,    12.82  ,  2.39 (            ---*--            ), 11.38,  12.82,  13.77
   4 ,         MWS1 ,    12.88  ,  1.98 (             --*--            ), 11.89,  12.88,  13.88
   4 ,          DE5 ,    12.92  ,  3.20 (            ---|*--           ), 11.24,  12.95,  14.44
   4 ,        MWS20 ,    12.94  ,  2.54 (            ---|*-            ), 11.45,  12.94,  14.00
   4 ,         MWS8 ,    13.01  ,  2.17 (             --|*-            ), 11.66,  13.01,  13.84
   4 ,         MWS3 ,    13.09  ,  2.03 (             --|*-            ), 11.99,  13.09,  14.02
   4 ,         DE20 ,    13.17  ,  1.35 (              -|*-            ), 12.38,  13.20,  13.73
   4 ,        MWS17 ,    13.22  ,  2.40 (             --|*--           ), 11.80,  13.22,  14.20
   5 ,         DE11 ,    13.25  ,  1.86 (              -|*-            ), 12.14,  13.28,  14.00
   6 ,          DE8 ,    13.61  ,  2.03 (               |-*--          ), 12.62,  13.66,  14.65
   6 ,          DE7 ,    13.65  ,  1.22 (               |-*-           ), 13.05,  13.65,  14.27
   6 ,         SA16 ,    13.67  ,  1.62 (               | *--          ), 13.35,  13.67,  14.97
   6 ,         DE15 ,    13.76  ,  2.40 (               |--*--         ), 12.65,  13.77,  15.04
   6 ,         DE16 ,    13.76  ,  1.68 (               |--*-          ), 13.09,  13.76,  14.77
   7 ,          SA6 ,    14.03  ,  3.07 (               | -*-----      ), 13.38,  14.03,  16.45
   7 ,          DE3 ,    14.17  ,  1.02 (               |  -*          ), 13.74,  14.17,  14.76
   7 ,          SA4 ,    14.27  ,  2.94 (               |---*--        ), 12.80,  14.27,  15.74
   7 ,          DE1 ,    14.27  ,  1.29 (               | --*          ), 13.58,  14.30,  14.88
   7 ,         DE18 ,    14.28  ,  1.52 (               |---*          ), 13.14,  14.29,  14.66
   7 ,         DE17 ,    14.36  ,  1.68 (               | --*-         ), 13.34,  14.38,  15.03
   7 ,          SA5 ,    14.37  ,  0.76 (               |   *          ), 14.21,  14.37,  14.97
   7 ,          SA2 ,    14.41  ,  2.23 (               |---*--        ), 13.20,  14.41,  15.43
   7 ,         SA13 ,    14.46  ,  1.92 (               |---*-         ), 13.21,  14.46,  15.13
   7 ,          SA3 ,    14.47  ,  1.18 (               | --*          ), 13.32,  14.47,  14.50
   7 ,         SA11 ,    14.48  ,  1.45 (               | --*-         ), 13.64,  14.48,  15.09
   8 ,         DE10 ,    14.57  ,  0.83 (               |   -*         ), 14.16,  14.57,  14.99
   8 ,          SA9 ,    14.70  ,  2.65 (               |  --*----     ), 14.09,  14.70,  16.74
   8 ,          SA1 ,    14.70  ,  1.91 (               |----*         ), 12.87,  14.70,  14.78
   8 ,         SA17 ,    14.74  ,  2.47 (               |----*-        ), 13.27,  14.74,  15.75
   9 ,         SA15 ,    15.06  ,  1.66 (               |   --*-       ), 14.16,  15.06,  15.82
   9 ,          SA7 ,    15.15  ,  1.57 (               |   --*        ), 14.24,  15.15,  15.81
   9 ,         SA12 ,    15.38  ,  2.54 (               | ----*-       ), 13.32,  15.38,  15.86
  10 ,         SA10 ,    15.50  ,  0.00 (               |      *       ), 15.50,  15.50,  15.50
  10 ,         SA20 ,    15.66  ,  0.90 (               |     -*       ), 15.04,  15.66,  15.94
  11 ,          SA8 ,    15.87  ,  1.31 (               |     --*      ), 15.13,  15.87,  16.44
  11 ,         SA14 ,    16.21  ,  0.68 (               |      -*      ), 15.53,  16.21,  16.21
  12 ,         SA19 ,    16.76  ,  1.39 (               |     ----*    ), 15.37,  16.76,  16.76
  12 ,         SA18 ,    16.98  ,  1.56 (               |      ---*    ), 15.70,  16.98,  17.26
```

Below is an overall performance chart: The eras for all 20 runs for each optimizer was collected to and plotted using Scott-Knott algorithm.
```unix

  rank ,         name ,    med   ,  iqr
  ----------------------------------------------------
     1 ,           DE ,    12.60  ,  2.16 (           ---*|-             ), 11.61,  12.60,  13.77
     1 ,          MWS ,    12.74  ,  2.18 (           ---*|-             ), 11.67,  12.74,  13.85
     2 ,           SA ,    14.70  ,  2.03 (               |----*-        ), 13.56,  14.70,  15.60
```

We see that overall DE performs better than SA and MWS.
This is because Differential Evolution incrementally improves upon its existing candidates white Max Walk Sat and Simulated Annealing choose their candidates randomly.

This is also the reason that Differential evolution tends to terminate early as compared to Simulated Annealing and MaxWalk Sat.

### Related Work
Eckart Zitzler and Simon Kunzli[3] describe how continuous domination proves to be a more effective way of comparing two candidates. This method has also been used in Geometric Active Learning for Search-Based Software Engineering[5] and On the Value of User Preferences in Search-Based Software Engineering: A Case Study in Software Product Lines[6]. Comparison between different optimizers based on various parameters has been explained in GALE[5].


### Threats to Validity
Optimizers look to explore the solution space in a quest to find the optimal solution. The method each optimizer follows is what differentiates them. Exploration takes time and methods like early termination may not allow the optimizers to reach a globally optimum solution. However in cases where efficiency preceded accuracy, early termination may be required. Thus
these optimizers should also be evaluated in according to the search space each of them has explored.

### Future Work
This experimentation has been performed on a single model that is DTLZ7 with 2 objectives and 10 decisions. This evaluation can be expanded to include more models with varying number of objectives,decisions. Additionally the problem explored in this experiment is a minimization problem. In the future models will different kinds of requirements can be explored to give a more complete evaluation of the optimizers.

### Conclusion
The experiment shows that Differential Evolution performed better on an average. This is mainly because it improves upon the current candidates to produce new ones. Simulated Anneali and Max WalkSat make more random jumps as compared to DE. This is also evident in the type2 results. due to the random jumps made, the eras produces my MWS and SA are not always similar. Thus resulting in a higher A12 value.

### Reference
[1] Storn, R.; Price, K. (1997). "Differential evolution - a simple and efficient heuristic for global optimization over continuous spaces". Journal of Global Optimization 11: 341-359. doi:10.1023/A:1008202821328.

[2] Storn, R. (1996). "On the usage of differential evolution for function optimization". Biennial Conference of the North American Fuzzy Information Processing Society (NAFIPS). pp. 519-523.

[3] Eckart Zitzler and Simon Kunzli Indicator-Based Selection in Multiobjective Search, Proceedings of the 8th International Conference on Parallel Problem Solving from Nature (PPSN VIII) September 2004, Birmingham, UK

[4] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan. 2002. A fast and elitist multiobjective genetic algorithm: NSGA-II. Trans. Evol. Comp 6, 2 (April 2002), 182-197. DOI=http://dx.doi.org/10.1109/4235.996017

[5] Krall J., ,Menzies T. , Davies M.2015. Geometric Active Learning for Search-Based Software Engineering. IEEE Computer Society

[6] Salam Sayyad, Tim Menzies, and Hany Ammar, On the Value of User Preferences in Search-Based Software Engineering: A Case Study in Software Product Lines, ICSE 2013.
