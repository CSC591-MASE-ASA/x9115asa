## A simple standard Genetic Algorithm

### Abstract
This paper discusses the implementation of Genetic Algorithms, findings and reasonings behind making various implementation decisions. This implementation follows the semantics of GA wherein a new generation of candidates are created by selecting, crossovering and mutating the previous generation of candidates. The discussion of the findings investigates and shows evidences that GA is a strong candidate in the class of evolutionary algorithms.

### Introduction
The basis of Genetic Algorithms is in selection of the fittest candidates and using them as a basis to produce a population of fitter candidates. The operations of selection, crossover and mutation mimic the biology process of evolution. Candidates inherit traits from their parents. If these traits help them survive and thrive, these candidates live on while unfit candidates die off. The population tends to become fitter due to this dying off and increased selection of fit candidates. (See concepts for detailed explanations of fitness).

Genetic Algorithms, like most evolutionary algorithms are used to derive optimum candidates according to their fitness. Fitness may involve maximizing, minimizing, converging or a combination of these across multiple (possibly independant) objectives. For example a genetic algorithm could be used to optimize candidates based on height and weight, to be fit for track sports.

In general, generations get progressively better and thus later generations of candidates are better (fitter) than previous generations.

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

### Implementation
Every run of GA consists of a population. A population is a list of generations in increasing chronological order. A generation is a list of candidates. Every candidates have some number of decisions and objectives (fitness). The number of decisions and objectives is fixed for every run of GA. The fitness of every candidate is calculated using DTLZ family of functions.

In total there are 20 runs of GA for every combination of number of objectives (2,4,6,8), number of decisions (10,20,40) and dtlz family(dtlz1 , dtlz3, dtlz5, dtlz7). The measures of hypervolume and spread are reported and discussed for these runs.

To compare the fitness of 2 candidates binary domination was used because fitness is a multi dimensional parameter. Every candidate has a number of decisions. These decision values are number in the continuous range of [0,1].

**GA operations**  
1. **Selection** - To select 2 candidates from a generation to perform crossover, the weighted wheel method was used. Every candidate gets a share of the wheel proportional to how many other candidates it dominates. The wheel is then spun (a random number is generated) and the candidate on which it falls on, is selected. This method allows for selection of fitter candidates with increased probability while not needing to aggregate multi dimensional parameters since this method uses binary domination.  
2. **Crossover** - Crossover between two candidates produces two children by choosing an arbitrary crossover point and copying over the decision values from the 1st half of the first candidate and 2nd half of the second candidate and vice versa. This produces 2 children who have a mixture of the decision values of their parents. This mixtureis one of the elements of introducing candidates with variation witha salt of it being favorable variation.  
3. **Mutation** - With certain probability a decision of the candidate is mutated i.e. it's value is changed. Mutation also contributes to the variations needed by the new generation. This slight variation allows for candidates to be generated with most decisions being similar but only different in some.

Pareto frontier is constructed using the last generation of GA, this being theoretically the best generation, since that's what the algorithm strives for. Using the last generation as base, the pareto front was built as follows
* Pick a random candidate from the frontier
* Pick a random candidate from elsewhere
* Compare the 2  
  1. If the frontier candidate dominates the other one, do nothing
  2. If the other candidate dominates the frontier candidate, swap
  3. If no relation, add the other candidate to the frontier

Do this 100,000 times. At the end a pareto frontier is obtained. The validity of the pareto front is checked by counting how many good picks (case 1) versus total number of picks. It was found to be between 80%-95% in most cases.

Once the pareto frontier is obtained, the hypervolume ratio is the ratio of candidates not in the pareto frontier to the total number of candidates.

The spread of the frontier is a vector of objectives, the values of which are the difference between the 75th and 25th percentile of the values of that objective for every candidate in the frontier.

Early termination is implemented using a12 for every 2 eras of 100 generations each. Using the standard threshold of 0.56, if the a12 value of the 2 eras is more than 0.56 , the algorithm is terminated.

##### Implementation decisions
1. After selection, crossover and mutation, the 2 generated children are directly put into the new generation without comparison. It was experimented with to compare the children with the parents and to only insert the better of the comparisons in the new generation, but it was found that in many cases after a certain 100 number of generations, the entire generation would become clones of a certain candidate with very little variation. Since this is undesirable in a genetic algorithm where diversity is needed to explore paths to the optimum solution, this choice was implementation was dropped.

2. To calculate hyper volume, using a random selection with *n* number of picks instead of doing *n<sup>2</sup>* all pairs comparisons for finding the pareto frontier. This method of building the pareto frontier proved to be robust with 80-95% of picks being good.

3. Spread is calculated as the difference between 75th and 25th percentile for every objective values for candidates in the frontier. This prevents outliers from influencing the spread.

#### Instructions to run the code
* [code9.py](https://github.com/CSC591-MASE-ASA/x9115asa/blob/master/hw/code/9/code9.py) - This is the main python script that contains the GA logic and exports runnable methods and classes that be imported like class GA which can be instantiatedby passing in parameterslike num_objs, num_decs, etc. Calling the `run` method will initiate the GA and return the metrics after the run.  
Sample codes are included at the bottom of the file  
* [dtlz.py](https://github.com/CSC591-MASE-ASA/x9115asa/blob/master/hw/code/9/dtlz.py) - The family of DTLZ functions to be used by `code9.py`.  
* [hve.py](https://github.com/CSC591-MASE-ASA/x9115asa/blob/master/hw/code/9/hve.py) - Module that does the calculation of hypervolume and spread at the end of every GA run
* [sk.py](https://github.com/CSC591-MASE-ASA/x9115asa/blob/master/hw/code/9/sk.py) - Skott Knott methods used to calculate a12
* [data/](https://github.com/CSC591-MASE-ASA/x9115asa/tree/master/hw/code/9/data) - This folder contains the output metrics for the various runs of GA.

All runs of GA take quite a while to run. Around 12 hours for 960 runs (20 runs for each of the combination of objectives, decisions and fitness family)

### Findings
##### Hyper volume ratios

The results for hypervolumes for every combination of objectives, decisions and fitness family (for 20 runs each) show that  
* Hypervolume ratio goes down with increase in number of objectives
* DTLZ1 and DTLZ7 are relatively less affected by number of objectives than DTLZ3 and DTLZ5
* Number of decisions has low effect on the hypervolume ratio

**dtlz1**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.965311±0.180911|0.9367±0.22583|0.928354±0.052384|
|4|0.841812±0.200012|0.880821±0.134431|0.8460495±0.1524595|
|6|0.7169855±0.1956755|0.764492±0.150402|0.7050465±0.3167165|
|8|0.5401645±0.2428455|0.6887655±0.3689855|0.630037±0.273197|

**dtlz3**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.96568±0.02366|0.956126±0.067156|0.9330675±0.1569175|
|4|0.844353±0.136153|0.883808±0.075818|0.838792±0.144272|
|6|0.650662±0.192898|0.8249865±0.1467965|0.740242±0.279412|
|8|0.6195875±0.1943475|0.7674625±0.1246825|0.7066965±0.2440665|

**dtlz5**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.87243±0.06151|0.852653±0.253633|0.893782±0.192522|
|4|0.5606255±0.2625845|0.7761495±0.0861295|0.657644±0.404634|
|6|0.4952295±0.2878795|0.6095815±0.3219415|0.5447855±0.4274855|
|8|0.3972285±0.3175385|0.4894435±0.2762935|0.3585875±0.4211525|

**dtlz7**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.964742±0.041742|0.9646155±0.1453255|0.9671045±0.1484145|
|4|0.969441±0.043931|0.9602375±0.1675375|0.9242355±0.2186555|
|6|0.955885±0.163865|0.9508245±0.1626845|0.8912205±0.2534205|
|8|0.947217±0.059087|0.9104205±0.1292905|0.8853775±0.1455575|

#### Spread
Spreads are reported in the [data/](https://github.com/CSC591-MASE-ASA/x9115asa/tree/master/hw/code/9/data) folder for every corresponding run of GA.  
* DTLZ3 produces large values for spread in all instances
* DTLZ1, 5, 7 maintain low values of spread for most of the instances with slight increase with increase in number of decisions

### Discussion
GA, being an evolutionary algorithm, tries to solve the problem of finding an optimum solution without knowing what direction it might be in or even have a base point to start of with. To do this, it relies on great deal of randomness and using previously generated values to approach the optimum. Given these constraints GA seems to perform well and with much less complexity than standard all pairs or mathematical resolution of the problem space. The validity of GA as an evolutionary algorithm can be verified with parameters such as hypervolume and spread, both of which are easy to calculate given the generations of a GA run.

This implementation paired with DTLZ family of fitness functions allows GA to venture into the realm of multi objective optimization. The results produced by this paper show that GA can be applied effectively to multi objective optimization although the confidence with higher number of objectives is not great. Tweaks to the current implementation like using continuous implementation may help fine tune GA for higher number of objectives.

#### Discussion of Findings
The reduction in hypervolume ratio with increase in number of objectives can be justified by the fact that binary domination gets less effective in comparing candidates as the number of objectives increase. Thus many candidates will have no relation to each other and gets tougher to construct the pareto frontier.

Since the decisions are transformed into fitness by DTLZ, the number of decisions doesn't really affect GA. Fitness values produced by more decisions may be different but they still are able to drive GA to an optimum.

#### Threats to validity
The basis of the generations getting better is the selection mechanism used to choose fit candidates from a generation. The implemented selection mechanism chooses candidates by a weighted wheel given a share of the wheel proportional to the number of other candidates it dominates in the generation. It is possible that, since the overall generation gets better together and not individual candidates, that candidates don't really dominate any (or few) candidates in their respective generations. After a while, the selection will transform into uniform random in a generation and will start producing non-optimal candidates. This implementation has not found any evidence of this scenario because spread values conform between runs.

#### Future Work
Binary domination is known to be questionable when dealing with number of objectives more than 2. Continuous domination could be used as method for comparing candidates based on their multi objective fitness. Binary domination, given it's binary decision decision making, will produce coarse grained outcomes with many candidates not being included in the pareto frontier. Continuous domination could finer outcomes allowing more candidates to be part of the pareto front will still maintaining low spread.

An additional technique for selection could be to constructthe pareto frontier for every generation and picking candidates from it for consideration for the next generation. This technique could produce a more focused (less spread) pareto frontier especially when paired with continuous domination.

### Conclusion
Genetic Algorithm is a promising algorithm in the class of Evolutionary Algorithms. It works well with existing fitness models and can accept a variety of decisions and objectives. It scales well for large number of candidates. The results of GA are easy to analyse and improve upon.

### References
1. Deb, Kalyanmoy, et al. [Scalable test problems for evolutionary multiobjective optimization](http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf). Springer London, 2005.

2.  GA concepts adapted from [Dr. Mark Humphrey's notes](http://computing.dcu.ie/~humphrys/Notes/GA/Code/code.ga.html), School of Computing. Dublin City University

3. DTLZ recreated in python following C++ implementation by [PAGMO](https://github.com/esa/pagmo/blob/master/src/problem/dtlz.cpp) library.