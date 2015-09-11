### Reference
H. J. Goldsby, P. Sawyer, N. Bencomo, D. Hughes, and B. H. Cheng. Goal-based modeling of dynamically adaptive system requirements. 15th Annual IEEE In- ternational Conference on the Engineering of Computer Based Systems (ECBS), 2008.

### Keywords
**ii1 Dynamically Adaptive Systems**

Systems capable of self adaptation at run-time so that the target goal of the system is achieved in spite of the dynamic change in requirements at execution time.

**ii2 MDD**

MDD stands for Model driven development which refers to the methodology of using models (artifacts of the proposed solution) to develop the software..

**ii3 LoREM**

Refers to a the Levels of Requirements Engineering for Modeling described by the authors in such a way that provides separation of concerns for the developers of a dynamically adaptive system.

**ii4 adaptation infrastructure**

It is set of mechanisms that enable adaptation in order for the system to react to the changes in the requirements to occur.

### Feature Extraction
**iii1 Related Work**

1. Below papers discuss level 1 of LoRem.

  i. M.S.Feather,S.Fickas,A.V.Lamsweerde,andC.Ponsard. Reconciling system requirements and runtime behavior. In IWSSD ’98: Proceedings of the 9th International Workshop on Software Specification and Design, 1998.

  ii. S.FickasandM.S.Feather.Requirementsmonitoringindy- namic environments. In RE ’95: Proceedings of the Second IEEE International Symposium on Requirements Engineer- ing, 1995.

  iii. Y. Yu, J. C. S. do Prado Leite, and J. Mylopoulos. From goals to aspects: Discovering aspects from requirements goal models. In Proceedings of the 12th IEEE International Con- ference on Requirements Engineering (RE 2004), 2004.

  iv. Y. Yu, J. Mylopoulos, A. Lapouchnian, S. Liaskos, and J. C. Leite. From stakeholder goals to high-variability software design. Technical report csrg-509, University of Toronto, 2005.

  v. A. Lapouchnian, S. Liaskos, J. Mylopoulos, and Y. Yu. To- wards requirements-driven autonomic systems design. In DEAS ’05: Proceedings of the 2005 Workshop on Design and Evolution of Autonomic Application Software, 2005.

**iii2 Future work**

The authors of the paper point to the limitations of the current system and suggest that more work needs to be done to evaluate if DASs could perform RE at runtime. Also new techniques to help system developers identify and generate models of candidate target systems that handle potentially adverse conditions in a robust manner need to be developed. Further they suggest human-generated behavioral models need to be incorporated into the current research.

**iii3 Sampling procedures**

The current hypothesis is studied by implementing it for a flood warning system called GridStix. A detailed explanation of the technology-driven process for performing RE is presented.

**iii4 Patterns**

Using RE process models Application-Driven RE Process or Technology-Driven RE Process offers three key benefits.

  a. separation of concerns for the developers

  b. produces models that can be used to guide the design of a DAS

  c. this approach provides more flexi- bility in defining process models for performing RE for a DAS.

### Improvement possibilities

**iv1 New results** :

The current system has been explained in detail along with a case study, however some mention on how to best handle future problems could help researchers or students in the field.

**iv2 Tutorial materials** :

Since the area of runtime requirement-monitoring and self repairing system is fairly new, tutorial materials could help researchers and students in the field gain a better understanding of the concept and the available material on the subject.

**iv3 Anti-Patterns** :
DAS being a highly dynamic system with complex RE required to implement self adaptation, the authors could have included few cautions to be aware of when doing this kind of work.

### Connection to previous paper
This paper serves as a precursor to Paper 1. Paper 1 explains the actual practical implementation of the theoretical idea presented in this paper along with concrete baseline results depicting accuracy of such systems.
