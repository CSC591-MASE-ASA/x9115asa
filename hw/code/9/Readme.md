## Code 9 - A simple standard genetic algorithm

#### Abstract
This paper discusses the implementation of Genetic Algorithms, findings and reasonings behind making various implementation decisions. This implementation follows the semantics of GA wherein a new generation of candidates are created by selecting, crossovering and mutating the previous generation of candidates. The specifics of these operations are discussed ahead.

#### Introduction
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

#### Implementation



#### Findings
##### Hyper volume ratios

**dtlz1**

|Num. Objs\Num. Decs|10|20|40|
|:---:|---|---|---|
|2|0.9607725±0.1924725|0.9374455+-0.1178055|0.9324275+-0.0594975|
|4|0.837854±0.191264|0.8744615+-0.0967715|0.8004585+-0.473998
|6|0.7061995±0.2644495|0.7807255+-0.1464555
|8|0.538669±0.273869|0.7295385+-0.1556285


#### Discussion

#### Conclusion