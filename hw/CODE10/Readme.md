## Using Differential Evolution to Tune Genetic Algorithm Parameters

### Abstract
We have seen how to implement Evolutionary Algorithms in [Code 9](https://github.com/CSC591-MASE-ASA/x9115asa/tree/master/hw/CODE9). In this experiment we aim to optimize the optimizer i.e. use the Differential Evolution (DE) optimizer to find out if we can achieve better results for the calculation of spread and hyper volume for a candidate population. This report presents a comparison between the results of tuned and untuned execution of GA. We will first execute the DE algorithm to find the optimum list of parameters that can be fed to the GA. We will then execute the algorithm for both default and tuned parameter values. We will then use the Scott-Knott statistical machinery to compare the results.

### Background
#### Genetic (Evolutionary) Algorithms

Aniket TODO

#### Differential Evolution
Differential evolution (DE) is a method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. Such methods are commonly known as meta heuristics as they make few or no assumptions about the problem being optimized and can search very large spaces of candidate solutions. However, meta heuristics such as DE do not guarantee an optimal solution is ever found.

DE is used for multidimensional real-valued functions but does not use the gradient of the problem being optimized, which means DE does not require for the optimization problem to be differentiable as is required by classic optimization methods such as gradient descent and quasi-newton methods. DE can therefore also be used on optimization problems that are not even continuous, are noisy, change over time, etc.

DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones according to its simple formulae, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. In this way the optimization problem is treated as a black box that merely provides a measure of quality given a candidate solution and the gradient is therefore not needed.


### Scott-knott
Scott-Knott (SK) is a hierarchical clustering algorithm used as an exploratory data analysis too. The SK procedure uses a clever algorithm of cluster analysis, where, starting from the whole group of observed mean effects, it divides, and keeps dividing the subgroups in such a way that the intersection of any of the two formed groups remains empty. In the words of A.J. Scott and M. Knott: "We study the consequences of using a well-known method of cluster analysis to partition the sample treatment means in a balanced design and show how a corresponding likelihood ratio test gives a method of judging the significance of the difference among groups obtained".[7]
### Implementation and results
The GA program uses the following input parameters to run
1. Optimizer: dtlz1, dtlz3, dtlz5 & dtlz7
2. Number of objectives: 2/4/6/8
3. Number of decisions: 10/20/40
4. Mutation rate: Determined my DE (Default: 5% for untuned runs)
5. Number of rate per generation: Determined by DE (Default: 100 for untuned runs)
6. Number of generations: Determined by DE (Default: 1000 for untuned runs)



##### Dominance comparator:
This comparator is used to compare two candidate solutions. This comparator is used when the optimizers are comparing pairs of candidates as each of the optimizers generate solutions
In order to do this we have used binary domination.

```python
def __gt__(self, other):
        if self.fitness == other.fitness:
            return False
        for i in xrange(candidate.num_objs):
            if other.fitness[i] < self.fitness[i]:
                return False
        return True
```

We used binary over continuous domination domination since continuous domination did not scale well for the large magnitude of runs performed. As the same comparison operators would be used for both tuned and untuned runs we are measuring the difference in results by focussing more on the delta factor between the two runs than the actual values.  


##### Pareto Frontier Maintenance 
It is important to maintain the pareto frontier across generations of the algorithm and update the frontier as new populations are created. The code snippet for updating the frontier when a new population is formed by cross over and mutation is shown below.
```python
def update_pareto(self, new_pareto):
        add_new = []
        for new in new_pareto:
            for old in self.pareto_frontier:
                if new > old:
                    self.pareto_frontier.remove(old)
                if not old > new and not old==new:
                    add_new.append(new)
                    break
        self.pareto_frontier.extend(add_new)
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



##### rdivDemo Method
This comparator is used to compare the final era generated by the optimizers.
The performance statistic used in this case is the aggregate of the objectives.
The algorithm followed was:

- When comparing N optimizers for R repeats..

- For each repeat, generate one new baseline, then...

- Run each optimizer for each repeat.

For this experiment R = 20
and N = 3 i.e DE, MWS and SA

The final era of each is represented in the Scott-Knott charts. The name of each row = Optimizer name(DE/SA/MWS) + repeat number (from 1..20)

Output:
```unix
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 , dtlz1_o8_d40_u ,    0.07  ,  0.01 (*              |              ), 0.07,  0.07,  0.08
   1 , dtlz5_o8_d40_u ,    0.08  ,  0.01 (*              |              ), 0.07,  0.08,  0.08
   1 , dtlz5_o8_d10_u ,    0.08  ,  0.01 (*              |              ), 0.07,  0.08,  0.09
   1 , dtlz5_o8_d20_u ,    0.08  ,  0.01 (*              |              ), 0.07,  0.08,  0.09
   1 , dtlz1_o8_d40_t ,    0.08  ,  0.00 (*              |              ), 0.08,  0.08,  0.08
   2 , dtlz1_o8_d20_u ,    0.10  ,  0.01 ( *             |              ), 0.09,  0.10,  0.11
   2 , dtlz1_o6_d40_u ,    0.10  ,  0.01 ( *             |              ), 0.10,  0.10,  0.11
   2 , dtlz5_o6_d10_u ,    0.11  ,  0.01 ( *             |              ), 0.10,  0.11,  0.11
   2 , dtlz5_o6_d40_u ,    0.11  ,  0.02 ( *             |              ), 0.11,  0.11,  0.12
   2 , dtlz5_o6_d20_u ,    0.12  ,  0.01 ( *             |              ), 0.11,  0.12,  0.12
   3 , dtlz1_o8_d20_t ,    0.14  ,  0.01 (  *            |              ), 0.13,  0.14,  0.14
   3 , dtlz3_o8_d40_u ,    0.14  ,  0.02 (  *            |              ), 0.13,  0.14,  0.15
   3 , dtlz1_o6_d40_t ,    0.14  ,  0.01 (  *            |              ), 0.13,  0.14,  0.15
   3 , dtlz7_o8_d40_u ,    0.15  ,  0.01 (  *            |              ), 0.14,  0.15,  0.16
   3 , dtlz1_o6_d20_u ,    0.15  ,  0.02 (  *            |              ), 0.13,  0.15,  0.15
   4 , dtlz5_o8_d40_t ,    0.16  ,  0.00 (   *           |              ), 0.16,  0.16,  0.16
   4 , dtlz7_o8_d20_u ,    0.16  ,  0.02 (   *           |              ), 0.15,  0.16,  0.18
   4 , dtlz7_o8_d40_t ,    0.16  ,  0.01 (   *           |              ), 0.16,  0.16,  0.16
   5 , dtlz1_o6_d20_t ,    0.17  ,  0.01 (   *           |              ), 0.16,  0.17,  0.18
   6 , dtlz1_o8_d10_u ,    0.18  ,  0.04 (   *           |              ), 0.17,  0.18,  0.21
   6 , dtlz3_o8_d20_u ,    0.18  ,  0.04 (   -*          |              ), 0.17,  0.18,  0.21
   6 , dtlz5_o6_d40_t ,    0.18  ,  0.01 (   -*          |              ), 0.18,  0.19,  0.19
   6 , dtlz7_o8_d20_t ,    0.19  ,  0.01 (    *          |              ), 0.18,  0.19,  0.19
   6 , dtlz3_o6_d40_u ,    0.19  ,  0.01 (   -*          |              ), 0.18,  0.19,  0.20
   6 , dtlz7_o8_d10_u ,    0.19  ,  0.01 (   -*          |              ), 0.18,  0.19,  0.20
   6 , dtlz5_o8_d20_t ,    0.20  ,  0.01 (    *          |              ), 0.19,  0.20,  0.20
   6 , dtlz5_o8_d10_t ,    0.20  ,  0.01 (    *          |              ), 0.20,  0.20,  0.21
   6 , dtlz3_o8_d40_t ,    0.21  ,  0.02 (    *          |              ), 0.19,  0.21,  0.21
   6 , dtlz7_o8_d10_t ,    0.21  ,  0.01 (    -*         |              ), 0.21,  0.21,  0.22
   6 , dtlz5_o4_d10_u ,    0.22  ,  0.02 (     *         |              ), 0.22,  0.22,  0.23
   6 , dtlz1_o4_d40_u ,    0.23  ,  0.02 (     *         |              ), 0.22,  0.23,  0.24
   6 , dtlz5_o6_d20_t ,    0.23  ,  0.01 (     *         |              ), 0.23,  0.23,  0.24
   6 , dtlz1_o6_d10_u ,    0.24  ,  0.04 (    -*         |              ), 0.21,  0.24,  0.25
   6 , dtlz5_o4_d20_u ,    0.24  ,  0.03 (     *         |              ), 0.23,  0.24,  0.26
   6 , dtlz5_o4_d40_u ,    0.25  ,  0.03 (     -*        |              ), 0.24,  0.25,  0.27
   6 , dtlz3_o6_d40_t ,    0.25  ,  0.02 (     -*        |              ), 0.24,  0.25,  0.26
   6 , dtlz1_o4_d40_t ,    0.25  ,  0.04 (     -*        |              ), 0.24,  0.25,  0.28
   6 , dtlz3_o6_d20_u ,    0.25  ,  0.03 (     -*        |              ), 0.23,  0.25,  0.26
   7 , dtlz1_o8_d10_t ,    0.26  ,  0.02 (      *        |              ), 0.26,  0.26,  0.27
   7 , dtlz3_o8_d20_t ,    0.27  ,  0.01 (      *        |              ), 0.26,  0.27,  0.28
   7 , dtlz3_o8_d10_u ,    0.27  ,  0.06 (     -*        |              ), 0.24,  0.27,  0.29
   8 , dtlz5_o6_d10_t ,    0.29  ,  0.01 (       *       |              ), 0.28,  0.29,  0.29
   8 , dtlz1_o6_d10_t ,    0.29  ,  0.02 (       *       |              ), 0.28,  0.29,  0.30
   9 , dtlz1_o4_d20_t ,    0.30  ,  0.01 (       *       |              ), 0.30,  0.30,  0.31
   9 , dtlz1_o4_d20_u ,    0.31  ,  0.02 (       -*      |              ), 0.30,  0.31,  0.33
  10 , dtlz7_o6_d40_u ,    0.32  ,  0.03 (        *      |              ), 0.31,  0.32,  0.34
  11 , dtlz3_o6_d10_u ,    0.34  ,  0.05 (        -*     |              ), 0.32,  0.34,  0.37
  11 , dtlz3_o6_d20_t ,    0.34  ,  0.01 (        -*     |              ), 0.34,  0.34,  0.35
  11 , dtlz5_o4_d40_t ,    0.35  ,  0.01 (         *     |              ), 0.34,  0.35,  0.35
  11 , dtlz7_o6_d40_t ,    0.35  ,  0.01 (         *     |              ), 0.35,  0.35,  0.36
  12 , dtlz5_o4_d10_t ,    0.36  ,  0.02 (         *     |              ), 0.35,  0.36,  0.37
  12 , dtlz3_o4_d40_t ,    0.37  ,  0.02 (         -*    |              ), 0.37,  0.37,  0.38
  12 , dtlz3_o4_d40_u ,    0.38  ,  0.02 (         -*    |              ), 0.37,  0.38,  0.39
  12 , dtlz7_o6_d20_u ,    0.38  ,  0.04 (         -*    |              ), 0.35,  0.38,  0.39
  12 , dtlz7_o6_d20_t ,    0.38  ,  0.01 (          *    |              ), 0.38,  0.38,  0.38
  12 , dtlz3_o8_d10_t ,    0.39  ,  0.03 (          *    |              ), 0.38,  0.39,  0.42
  12 , dtlz5_o4_d20_t ,    0.39  ,  0.00 (          *    |              ), 0.39,  0.39,  0.40
  12 , dtlz3_o6_d10_t ,    0.40  ,  0.02 (          -*   |              ), 0.39,  0.40,  0.42
  13 , dtlz7_o6_d10_t ,    0.43  ,  0.01 (           *   |              ), 0.43,  0.43,  0.43
  14 , dtlz3_o4_d20_t ,    0.46  ,  0.01 (            *  |              ), 0.46,  0.46,  0.47
  14 , dtlz1_o4_d10_t ,    0.46  ,  0.05 (            -* |              ), 0.45,  0.47,  0.50
  14 , dtlz7_o6_d10_u ,    0.47  ,  0.05 (            -* |              ), 0.45,  0.47,  0.49
  14 , dtlz1_o4_d10_u ,    0.48  ,  0.07 (            -* |              ), 0.45,  0.48,  0.52
  15 , dtlz3_o4_d20_u ,    0.51  ,  0.03 (              *|              ), 0.50,  0.51,  0.53
  16 , dtlz3_o4_d10_t ,    0.57  ,  0.05 (               |*             ), 0.55,  0.57,  0.60
  17 , dtlz5_o2_d10_u ,    0.60  ,  0.03 (               |-*            ), 0.59,  0.60,  0.62
  17 , dtlz3_o4_d10_u ,    0.61  ,  0.04 (               | *            ), 0.60,  0.61,  0.64
  18 , dtlz7_o4_d20_t ,    0.65  ,  0.14 (               | --*-         ), 0.60,  0.68,  0.74
  18 , dtlz5_o2_d20_u ,    0.76  ,  0.02 (               |      *       ), 0.76,  0.76,  0.78
  18 , dtlz7_o4_d40_u ,    0.78  ,  0.06 (               |     --*      ), 0.73,  0.78,  0.79
  18 , dtlz7_o4_d40_t ,    0.78  ,  0.08 (               |     --*      ), 0.74,  0.79,  0.82
  19 , dtlz5_o2_d10_t ,    0.85  ,  0.01 (               |         *    ), 0.85,  0.85,  0.86
  20 , dtlz5_o2_d20_t ,    0.86  ,  0.01 (               |         *    ), 0.86,  0.86,  0.86
  20 , dtlz1_o2_d40_t ,    0.86  ,  0.02 (               |         *    ), 0.85,  0.86,  0.87
  20 , dtlz5_o2_d40_u ,    0.86  ,  0.01 (               |         *    ), 0.86,  0.86,  0.87
  21 , dtlz5_o2_d40_t ,    0.88  ,  0.01 (               |          *   ), 0.88,  0.88,  0.89
  22 , dtlz1_o2_d40_u ,    0.92  ,  0.01 (               |           *  ), 0.92,  0.92,  0.93
  22 , dtlz1_o2_d10_u ,    0.92  ,  0.02 (               |           *  ), 0.91,  0.92,  0.93
  22 , dtlz3_o2_d10_u ,    0.92  ,  0.02 (               |           *  ), 0.92,  0.93,  0.94
  22 , dtlz7_o2_d20_u ,    0.93  ,  0.01 (               |           *  ), 0.93,  0.93,  0.94
  22 , dtlz1_o2_d20_u ,    0.93  ,  0.01 (               |           *  ), 0.93,  0.93,  0.94
  22 , dtlz7_o2_d40_t ,    0.93  ,  0.01 (               |           *  ), 0.93,  0.93,  0.94
  22 , dtlz7_o2_d10_u ,    0.94  ,  0.01 (               |           -* ), 0.93,  0.94,  0.94
  22 , dtlz7_o4_d20_u ,    0.94  ,  0.04 (               |           -* ), 0.91,  0.94,  0.95
  22 , dtlz7_o2_d40_u ,    0.94  ,  0.01 (               |            * ), 0.94,  0.94,  0.94
  22 , dtlz1_o2_d10_t ,    0.94  ,  0.01 (               |            * ), 0.94,  0.94,  0.95
  22 , dtlz1_o2_d20_t ,    0.94  ,  0.01 (               |           -* ), 0.94,  0.94,  0.95
  22 , dtlz3_o2_d40_t ,    0.94  ,  0.01 (               |           -* ), 0.94,  0.94,  0.95
  22 , dtlz3_o2_d20_u ,    0.95  ,  0.01 (               |            * ), 0.95,  0.95,  0.96
  22 , dtlz3_o2_d40_u ,    0.95  ,  0.01 (               |            * ), 0.95,  0.95,  0.96
  22 , dtlz3_o2_d20_t ,    0.96  ,  0.01 (               |            * ), 0.95,  0.96,  0.96
  22 , dtlz3_o2_d10_t ,    0.96  ,  0.01 (               |            * ), 0.96,  0.96,  0.96
  22 , dtlz7_o2_d20_t ,    0.96  ,  0.01 (               |            * ), 0.96,  0.96,  0.96
  22 , dtlz7_o4_d10_u ,    0.97  ,  0.03 (               |            -*), 0.95,  0.97,  0.98
  22 , dtlz7_o4_d10_t ,    0.97  ,  0.02 (               |            -*), 0.97,  0.97,  0.99
  22 , dtlz7_o2_d10_t ,    0.98  ,  0.01 (               |             *), 0.98,  0.98,  0.99
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

[7] Electronic Document Format(APA) Jelihovschi, E.G., Faria, J.C., & Allaman, I.B.. (2014). ScottKnott: a package for performing the Scott-Knott clustering algorithm in R. TEMA (São Carlos), 15(1), 3-17. https://dx.doi.org/10.5540/tema.2014.015.01.0003
