### Reference

Whittle, Jon, Pete Sawyer, Nelly Bencomo, Betty HC Cheng, and Jean-Michel Bruel. "RELAX: a language to address uncertainty in self-adaptive systems requirement." Requirements Engineering 15, no. 2 (2010): 177-196.

### Keywords

* ii1 - **Non-invariant requirements** - Requirements that cannot be compromised or traded off for a variant requirement.
* ii2 - **Uncertainty factors** - The environment and monitored properties and their relations.
* ii3 - **Fuzzy set** - A set whose members posses degrees of membership and not necessarily boolean.
* ii4 - **Dynamically Adaptive Systems (DAS)** - Systems that dynamically self-adapt to changing environment conditions.

### Feature Extraction

* iii1- **New Results** - The authors of the paper have proposed and described a new language for describing requirements for a self-adaptive system. This new requirement specification language addresses the problem of describing requirements in a way to account for changing environment and runtime factors.


* iii2 - **Tutorial Materials** - The authors include an in-depth walkthrough through a sample application problem domain. They instruct the readers in the procedure of applying the new *RELAX* language in specifying requirements for the system and accounting for the various uncertainties involved. By following this walk-through they propose, the *RELAX* language can be applied to other problem scenarios as well.


* iii3 - **Related Work** -  
  1. Cheng et al. (2008) Software engineering for self-adaptive systems: a research road map, Dagstuhl-seminar on software engineering for self- adaptive systems. In: Software engineering for self-adaptive systems. Lecture Notes in Computer Science, Springer, Berlin, p 5525.  
  2. Lapouchnian A et al. (2006) Requirements-driven design of autonomic application software. In: Proceedings of CASCON  
  3. Yijun Y et al. (2008). From goals to high-variability software design, vol 4994. Springer, Berlin 	
  4. Morandini M, Penserini L, Perini A (2008) Modelling selfadaptivity: a goal-oriented approach. In: Proceedings of second IEEE international conference on self-adaptive and self-organizing systems (SASO), pp 469–470


* iii4 - **Future Work** - The authors propose to investigate work in apping *RELAX* requirements to implementation using adaptive infrastructure and frameworks. They also propose to investigate requirements analsysis techniques for *RELAX* requirements to gauge how effective and consistent RELAX requirements are for a system.


### Improvements

1. iv1 - The authors suggest that if a invariant requirement is identified, it is to be untouched in the the RELAX flow. Instead we can consider checking if the the requirement can be decomposed into variant and invariant and then operate on the variant part.

2. iv2 - The authors should explore describing requirements at different levels. In the paper the authors have described requirements at the lowest level mapped to lowest level properties of the system. The authors can explore if and how higher level requirements can be described in the *RELAX* language to describe adaptive goals.

3. iv3 - The sample application (AAL) is a smart home system which even though is a software system, heaviliy relies on hardware sensors for environment and monitored properties. However this is not true for many real world software. The authors should explore a system that relies on software signals as properties.

#### Relation to Paper One

The RELAX language proposed by the authors of this paper is an example of an implementation technique for the abstract runtime goal resolution concepts proposed in Paper One. The RELAX language allows goals to be specified in a way that complies with the idealogies proposed in Paper One by explicitly stating the variable properties and their relationships with each other and the goals. During runtime, these variables can be monitored for a effective assesment of goal satisfaction.