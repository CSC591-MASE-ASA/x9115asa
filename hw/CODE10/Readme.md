## Using Differential Evolution to Tune Genetic Algorithm Parameters

### Abstract
We have seen how to implement Evolutionary Algorithms in [Code 9](https://github.com/CSC591-MASE-ASA/x9115asa/tree/master/hw/CODE9). In this experiment we aim to optimize the optimizer i.e. use the Differential Evolution (DE) optimizer to find out if we can achieve better results for the calculation of spread and hyper volume for a candidate population. This report presents a comparison between the results of tuned and untuned execution of GA. We will first execute the DE algorithm to find the optimum list of parameters that can be fed to the GA. We will then execute the algorithm for both default and tuned parameter values. We will then use the Scott-Knott statistical machinery to compare the results.

### Background
#### Genetic (Evolutionary) Algorithms

The basis of Genetic Algorithms is in selection of the fittest candidates and using them as a basis to produce a population of fitter candidates. The operations of selection, crossover and mutation mimic the biological process of evolution. Candidates inherit traits from their parents. If these traits help them survive and thrive, these candidates live on while unfit candidates die off. The population tends to become fitter due to this dying off and increased selection of fit candidates. (See concepts for detailed explanations of fitness).

Genetic Algorithms, like most evolutionary algorithms are used to derive optimum candidates according to their fitness. Fitness may involve maximizing, minimizing, converging or a combination of these across multiple (possibly independant) objectives. For example a genetic algorithm could be used to optimize candidates based on height and weight, to be fit for track sports.

In general, generations get progressively better and thus later generations of candidates are better (fitter) than previous generations. This works even if the optimum soltution or even direction is unknown. GA can therefore be applied in such types of problems where optimum solution where even characteristics of optimum solution are unknown.

#### Differential Evolution
Differential evolution (DE) is a method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. Such methods are commonly known as meta heuristics as they make few or no assumptions about the problem being optimized and can search very large spaces of candidate solutions. However, meta heuristics such as DE do not guarantee an optimal solution is ever found.

DE is used for multidimensional real-valued functions but does not use the gradient of the problem being optimized, which means DE does not require for the optimization problem to be differentiable as is required by classic optimization methods such as gradient descent and quasi-newton methods. DE can therefore also be used on optimization problems that are not even continuous, are noisy, change over time, etc.

DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones according to its simple formulae, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. In this way the optimization problem is treated as a black box that merely provides a measure of quality given a candidate solution and the gradient is therefore not needed.


#### Scott-knott
Scott-Knott (SK) is a hierarchical clustering algorithm used as an exploratory data analysis too. The SK procedure uses a clever algorithm of cluster analysis, where, starting from the whole group of observed mean effects, it divides, and keeps dividing the subgroups in such a way that the intersection of any of the two formed groups remains empty. In the words of A.J. Scott and M. Knott: "We study the consequences of using a well-known method of cluster analysis to partition the sample treatment means in a balanced design and show how a corresponding likelihood ratio test gives a method of judging the significance of the difference among groups obtained".[7]

#### Terms
1. Candidates - An instance of a solution. A candidate has decisions and fitness
2. Decisions - Independent variables that are properties of every candidate and used to derive fitness
3. Fitness - A measure of optimality of a candidate based on it's objective values
4. Objectives - A derived value that can be minimized, maximised or converged to a value to determine how fit a candidate is
5. DTLZ - A family of functions that can output multi-objective functions that should be minimized and are optimum at a particular profile
6. Pareto Frontier - A set of candidates that dominate all other candidates
7. Hypervolume - A set of candidates dominated by the pareto frontier
8. Selection - The process of selecting a fit candidate from a generation
9. Crossover - The process of merging two candidates to produce two children
10. Mutation - The process of randomly varying decision values in a candidate
11. Binary domination - A candidate is said to binary dominate another candidate if its objective values are better in at least one instance and never worse


### Implementation and results

#### Differential Evolution Loop
We first run a DE loop to determine the ideal arguments that are to be used to run the GA. We achieve this by using a Tuner class as a model. The Tuner class comes with 3 decisions: mutation rate, number of candidates and number of generations. The objective function for this class is the value of hypervolume generated by running GA. 

For DE runs we have used a max tries value of 2 and the initial candidate pool of 15. This would effectively give us 30 runs of GA in DE internally. We believe this would enable us to find optimal parameters for running GA in tuned mode.

#### Genetic Algorithm Runs

Using the parameter list generated from the DE loop we are now in a position to run tuned GA for comparison with untuned GA. The GA program uses the following input parameters to run. <br />

1. Optimizer: dtlz1, dtlz3, dtlz5 & dtlz7
2. Number of objectives: 2/4/6/8
3. Number of decisions: 10/20/40
4. Mutation rate: Determined by DE loop (Default: 5% for untuned runs)
5. Number of rate per generation: Determined by DE (Default: 100 for untuned runs)
6. Number of generations: Determined by DE (Default: 1000 for untuned runs)



##### Dominance comparator:
This comparator is used to compare two candidate solutions of GA. This comparator is used when the optimizers are comparing pairs of candidates as each of the optimizers generate solutions
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

#### Result Generation and Analysis
The below steps indicate how the result generation was performed. <br />

1. Run the GA program 20 times for each mode of operation (tuned/untuned) and store the results as a list in a file. The file naming conventtion was 'model_noOfObj_noOfDecs_(t/u).lst' eg. dtlz1_o2_d10_t.lst
2. Merge the lists generated in step 1 and create a list of lists.
3. Use this as an input to the rdivDemo method.

##### rdivDemo Method
This comparator is used to compare and rank the runs for GA based on the values of hypervolume generated. The method was used in the following manner.
```python
from sk import rdivDemo
if __name__ == '__main__':
    rDiv_ip=[]
    for file in glob.glob('outputs/*lst'):
        with open(file, 'rb') as f:
            my_list = pickle.load(f)
            rDiv_ip.append(my_list)
    rdivDemo(rDiv_ip)
```
### Results
The output generated is in ranked as shown below in increasing order of hypervolume.

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

The performance statistics for tuned vs untuned is shown below. Out of a total number of runs of 48 each the tuned algorithm produces better values for hypervolume on 39 out of 48 runs.

| Mode      | No. of times performs better   |
|-----------|--------------------------------|
| Tuned     | 39                             |
| Untuned   | 9                              |

The model wise performance for tuned vs untuned mode is shown below.

| Model     | Better HV (Tuned/Untuned)      |
|-----------|--------------------------------|
| dtlz1     | 9/3                            |
| dtlz3     | 9/3                            |
| dtlz5     | 12/0                           |
| dtlz7     | 9/3                            |


#### Discussion of Findings
The reduction in hypervolume ratio with increase in number of objectives can be justified by the fact that binary domination gets less effective in comparing candidates as the number of objectives increase. Thus many candidates will have no relation to each other and gets tougher to construct the pareto frontier.

Since the decisions are transformed into fitness by DTLZ, the number of decisions doesn't really affect GA. Fitness values produced by more decisions may be different but they still are able to drive GA to an optimum.

### Threats to Validity
While this algorithm implementation manages to demonstrate that the DE implementation to tune the GA would definitely improve the quality of results produced by the untuned implementation, the quality of the pareto_frontier generated using binary domination is poor. The simplicity of this implementation guarantees a faster execution of the tuner but to obtain better results we need to explore better domination approaches. 

### Future Work
This experimentation has been performed comprehensively for varying number of objectives and decisions. We noticed that binary domination did not perform well for higher number of objectives. In the future a blazingly fast tournament selection alternative for binary domination should be explored to produce better results.

### Conclusion
The experiment shows that Differential Evolution has indeed improved the quality of input parameters to the GA. This is because the algorithm keeps improving the pool of candidates when the neighbor energy is better than the current energy. When the underlying optimizer is run multiple times using DE we are able to achieve better results by tuning the input after each run. This can greatly reduce the running time of algorithm by reducing the number of generations and the size of candidate pools in most cases.


### Reference
[1] Storn, R.; Price, K. (1997). "Differential evolution - a simple and efficient heuristic for global optimization over continuous spaces". Journal of Global Optimization 11: 341-359. doi:10.1023/A:1008202821328.

[2] Storn, R. (1996). "On the usage of differential evolution for function optimization". Biennial Conference of the North American Fuzzy Information Processing Society (NAFIPS). pp. 519-523.

[3] Eckart Zitzler and Simon Kunzli Indicator-Based Selection in Multiobjective Search, Proceedings of the 8th International Conference on Parallel Problem Solving from Nature (PPSN VIII) September 2004, Birmingham, UK

[4] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan. 2002. A fast and elitist multiobjective genetic algorithm: NSGA-II. Trans. Evol. Comp 6, 2 (April 2002), 182-197. DOI=http://dx.doi.org/10.1109/4235.996017

[5] Electronic Document Format(APA) Jelihovschi, E.G., Faria, J.C., & Allaman, I.B.. (2014). ScottKnott: a package for performing the Scott-Knott clustering algorithm in R. TEMA (São Carlos), 15(1), 3-17. https://dx.doi.org/10.5540/tema.2014.015.01.0003

[6] Deb, Kalyanmoy, et al. [Scalable test problems for evolutionary multiobjective optimization](http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf). Springer London, 2005.

[7]  GA concepts adapted from [Dr. Mark Humphrey's notes](http://computing.dcu.ie/~humphrys/Notes/GA/Code/code.ga.html), School of Computing. Dublin City University

[8] DTLZ recreated in python following C++ implementation by [PAGMO](https://github.com/esa/pagmo/blob/master/src/problem/dtlz.cpp) library.
