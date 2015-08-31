### Reference
Kristopher Welsh, Pete Sawyer and Nelly Bencomo. 2008. Towards Requirements Aware Systems: Run-time Resolution of Design-time Assumptions. 26th IEEE/ACM International Conference Automated Software engineering (ASE 11), IEEE, 2011.

### Keywords
**ii1 requirements awareness**

Requirement awareness is the ability of a system to optimize the strategy used for goal satisfaction in presence of a change in context.

**ii2 self adaptive systems**

Self adaptive systems are systems that are capable of improving their ability to react to a scenario to produce desirable goals using some kind of feedback mechanism after each iteration.

**ii3 goals**

The goal represents the main functionality of the system under consideration.


**ii4 claims**

Claims represent the rationale for selecting a particular strategy to achieve the goal amongst numerous alternative strategies that exist in order to achieve the same goal.

### Feature Extraction
**iii1 Related Work**

The below papers further explore various approaches of goal satisfaction using models like KAOS and RELAX  :

1. S. A. DeLoach and M. Miller, “A goal model for adaptive complex systems,” International Journal of Computa- tional Intelligence: Theory and Practice., vol. 5, no. 2, 2010.

2. E. Letier and A. van Lamsweerde, “Reasoning about partial goal satisfaction for requirements and design engineering,” in Proc. of 12th ACM SIGSOFT International Symposium on Foundations of Software Engineering, 2004, pp. 53–62.

3. A. van Lamsweerde, Requirements Engineering: From System Goals to UML Models to Software Specifications. John Wiley & Sons, 2009.

4. J. Whittle, P. Sawyer, N. Bencomo, B. H. C. Cheng, and J.-M. Bruel, “Relax: a language to address uncertainty in self-adaptive systems requirement,” Requirements Engineering, vol. 15, no. 2, pp. 177–196, 2010.

5. B. H. Cheng, P. Sawyer, N. Bencomo, and J. Whittle, “Goal-based modeling approach to develop requirements for adaptive systems with environmental uncertainty,” in ACM/IEEE 12th International Conference On Model Driven Engineering Languages And Systems, MOD- ELS’09, 2009.

6. L. Baresi and L. Pasquale, “Fuzzy goals for requirements-driven adaptation,” in 18th International IEEE Requirements Engineering Conference, RE’10, 2010.

**iii2 Sample models**

The current hypothesis is studied using GridStix, an experimental flood warning system. This offers an executable form of the hypothesis by applying REAssuRE with the help of goal models and Claim Refinement models to the GridStix system .

**iii3 Baseline results**

The authors of the paper were able to conclude that there was an improvement of 5% in the longevity when Grid-stix used claims. This result can be used as a baseline for further studies to determine whether the added complexity of the run-time model is justified by the improvement in longevity.

**iii4 Future work**

Towards the end of the paper , the authors point out that the results can be further improved upon by incrementally eliminate the i* modeling restrictions that currently apply to REAssuRE. Also they point out that effects of claim refutation should be propagated up the goal tree.
This gives motivation for further research into the field of requirement awareness in systems.

### Improvement possibilities

2. Provide Delivery tools : Providing delivery tools that would enable other researchers to rerun the analysis could help the readers of the paper gain a better understanding of the system studied.

2. Details on the Data : The authors mention that the  improvement in longevity was found to be about 5%. However , details on the data measured has not been mentioned or provided in the paper.

3. Provide more details on the evaluation of the results : It is mentioned that the results were calculated by "measuring the network’s life; the time taken for fragmen- tation of the network to reach a point where no result was returned in response to the prevailing river conditions. ". However more details on the calculation should have been provided.
