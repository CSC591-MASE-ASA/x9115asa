### Reference
Bencomo, Nelly, Amel Belaggoun, and Valerie Issarny. "Dynamic decision networks for decision-making in self-adaptive systems: a case study." Software Engineering for Adaptive and Self-Managing Systems (SEAMS), 2013 ICSE Workshop on. IEEE, 2013.

### Keywords
**ii1 Dynamic Decision Networks**

Dynamic Decision networks (DNs) extend Bayesian networks to provide a mechanism for making rational decisions by combining probability and utility theory over changes in variables over time.

**ii2 Bayesian network **

Bayesian network is a probabilistic model that represents a set of random variables or chance nodes and their conditional dependencies.

**ii3 Decision Node **

A decision node D<sub>t</sub> represents the decision taken when specifying the topology to be used in time slice t.

**ii4 Evidence Node **

The evidence node E<sub>t</sub> represents the information observed by monitorables.

### Feature Extraction
**iii1 Related Work**
1. Uncertainty for Self-Adaptation  
  * N. Esfahani, K. Razavi, and S. Malek, “Dealing with uncertainty in early software architecture,” in Proceedings of the ACM SIGSOFT 20th International Symposium on the Foundations of Software Engineering, ser. FSE ’12. New York, NY, USA: ACM, 2012, pp. 21:1–21:4.

  * P. Sawyer, N. Bencomo, E. Letier, and A. Finkelstein, “Requirementsaware systems: A research agenda for re self-adaptive systems,” in Proc. of the 18th IEEE International Requirements Engineering Conference, 2010, pp. 95–103.

2. Decision-Making under Bayesian Theory
  * L. Portinale and D. C. Raiteri, “Using dynamic decision networks and
extended fault trees for autonomous fdir,” in ICTAI, 2011, pp. 480–484.


**iii2 Baseline results**

The paper describes the procedure and provides results for applying the Dynamic Decision Network methodology to the Remote Data Mirroring application. It features the process of analysis of the problem domain in the DDN terms, deriving a Bayesian Network that describes the Functional and Non-Functional Requirements and providing the results of application of the same. This procedure and results can be used as comparison in other applications.

**iii3 Informative visualizations**

The authors provide useful visualizations of the system in effect and how the decisions made by the DDNs vary over time w.r.t. a system hat does not dynamically adapt to changing environmental factors.

**iii4 Future work**

The authors want to investigate how the DDN system can be applied to quanititative requirements and dealing with confidence intervals for given targets. Another proposed study is looking into how changes in the probabilities themselves affects the system and how they vary over time. They also suggest that development of tools to help design DDNs for be a beneficial effort to make.

### Improvement possibilities

**iv1 Patterns & Anti-Patterns** :

Since the paper attempts to address a new approach to define Dynamic Decision Network, the authors should investigate and present various ways in which the methodology can be effectively used and possibly abused.

**iv2 Sampling Procedures** :

The authors should outline how they went about evaluating problems domains and selecting the Remote Data Mirroring problem. As mentioned above, the authors should describe how the selected problem domain covers at least a representative portion of patterns.

**iv3 Study instruments** :

The authors should provide the scripts used to calculate the inference values or an explanation of the same. Without these scripts, the correlation between the data and the findings is not reproducible.

### Connection to previous paper
This paper outlines how Bayesian Networks and Dynamic Decision Networks are good implementations of the design of requirement aware systems. The work done in this paper satisfies some of the proposed future work mentioned in Paper 1 by realizing environmental factors that changes and making a decision to maintain a desired level of requirement satisfaction.
