## Code 9 - A simple standard genetic algorithm

### Abstract
This paper discusses the implementation of Genetic Algorithms, findings and reasonings behind making various implementation decisions. This implementation follows the semantics of GA wherein a new generation of candidates are created by selecting, crossovering and mutating the previous generation of candidates. The specifics of these operations are discussed ahead.

### Introduction
The basis of Genetic Algorithms is in selection of the fittest candidates and using them as a basis to produce a population of fitter candidates. The operations of selection, crossover and mutation mimic the biology process of evolution. Candidates inherit traits from their parents. If these traits help them survive and thrive, these candidates live on while unfit candidates die off. The population tends to become fitter due to this dying off and increased selection of fit candidates. (See concepts for detailed explanations of fitness).

Genetic Algorithms, like most evolutionary algorithms are used to derive optimum candidates according to their fitness. Fitness may involve maximizing, minimizing, converging or a combination of these accross multiple (possibly independant) objectives. For example a genetic algorithm could be used to optimize candidates based on height and weight, to be fit for track sports.

In general, generations get progressively better and thus later generations of candidates are better (fitter) than previous generations. 

#### Terms
1. Candidates - An instance of a solution. A candidate has decisions and fitness
2. Decisions - Independant variables that are properties of every candidate and used to derive fitness
3. Fitness - A measure of optimatality of a candidate based on it's objective values
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
1. **Selection** - To select 2 candidates from a generation to perform crossover, the weighted wheel method was used. Every candidate gets a share of the wheel proportional to how many other candidates it dominates. The wheel is then spun (a random number is generated) and the candidate on which it falls on, is selected. This method allows for selection of fitter candidates with increased probability while not needing to aggregate multi dimensional paramters since this method uses binary domination.  
2. **Crossover** - Crossover between two candidates produces two children by choosing an arbitrary crossover point and copying over the decision values from the 1st half of the first candidate and 2nd half of the second candidate and vice versa. This produces 2 children who have a mixture of the decision values of their parents. This misture is one of the elements of introducing candidates with variation wih a salt of it being favorable variation.  
3. **Mutation** - With certain probablity, a decision of the candidate is mutated i.e. it's value is changed. Mutation also contributes to the variations needed by the new generation. This slight variation allows for candidates to be generated with most decisions being similar but only different in some.

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

#### Instructions to run the code
* `code9.py` - This is the main python script that contains the GA logic and exports runnable methods and classes that be imported like class GA which can be intantiated by passing in paramters like num_objs, num_decs, etc. Calling the `run` method will initiate the GA and return the metrics after the run.  
* `dtlz.py` - The family of DTLZ functions to be used by `code9.py`.  
* `hve.py` - Module that does the calculation of hypervolume and spread at the end of every GA run
* `data/` - This folder contains the output metrics for the various runs of GA.

### Findings

##### Implementation decisions
1. After selection, crossover and mutation, the 2 generated children are directly put into the new generation without comparison. It was experimented with to compare the children with the parents and to only insert the better of the comparisons in the new generation, but it was found that in many cases after a certain 100 number of generations, the entire generation would become clones of a certain candidate with very little variation. Since this is undesirable in a genetic algorithm where diversity is needed to explore paths to the optimum solution, this choice was implementation was dropped.

2. To calculate hyper volume, using a random selection with *n* number of picks instead of doing *n<sup>2</sup>* all pairs comparisons for finding the pareto frontier. This method of building the pareto frontier proved to be robust with 80-95% of picks being good.

##### Hyper volume ratios

**dtlz1**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.965311±0.180911|0.9367±0.22583|0.928354±0.052384|
|4|0.841812±0.200012|0.880821±0.134431|0.8460495±0.1524595|
|6|0.7169855±0.1956755|0.764492±0.150402|0.7050465±0.3167165|
|8|0.5401645±0.2428455|

**dtlz3**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.96568+-0.02366|0.956126+-0.067156|0.9330675+-0.1569175|
|4|0.844353+-0.136153|0.883808+-0.075818|0.838792+-0.144272|
|6|0.650662+-0.192898|0.8249865+-0.1467965|0.740242+-0.279412|
|8|0.6195875+-0.1943475

**dtlz5**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.87243+-0.06151|0.852653+-0.253633|0.893782+-0.192522|
|4|0.5606255+-0.2625845|0.7761495+-0.0861295|0.657644+-0.404634|
|6|0.4952295+-0.2878795|0.6095815+-0.3219415|0.5447855+-0.4274855|
|8|

**dtlz7**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.964742+-0.041742|0.9646155+-0.1453255|0.9671045+-0.1484145|
|4|0.969441+-0.043931|0.9602375+-0.1675375|0.9242355+-0.2186555|
|6|0.955885+-0.163865|0.9508245+-0.1626845|0.8912205+-0.2534205|
|8|

#### Discussion

#### Conclusion