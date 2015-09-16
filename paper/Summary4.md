#### Reference

DeLoach, Scott A., and Matthew Miller. "A goal model for adaptive complex systems." International Journal of Computational Intelligence: Theory and Practice 5.2 (2010): 83-92.

#### Keywords

1. ii1 - **Goal classes** - goals that are specified by the system designer to model the goal interactions within the organization.
2. ii2 - **Goal instances**  -The runtime instantiation of a goal class with specific parameters.
3. ii3 - **Goal Specification tree** - A GMoDS goal specification tree (GSpec) specifies how the goal classes are related to one another.
4. ii4 - **Goal Triggers** - A set of relations within the tree structure to specify how runtime goals may interact.

#### Feature Extraction

* iii1 - **Future Work** - The authors propose to extend the presented work by taking into account soft goals, goal preferences and goal metrics into their GMoDS goal model.


* iii2 - **Informative Visualisations** - The authors have illustrated their concepts of goal specification, instantiation and realization through visualizations like graphs and trees. These media are powerful instructors because relationships between entities like depends, precredes and consists of, are best explained visually.


* iii3 - **Related Work** - The authors have identified several related studies and frameworks
  1. Knowledge Acquisition in automated Specification (KAOS) framework - van Lamsweerde, A. and Letier, E. 2000. Handling Obstacles in Goal-Oriented Requirements Engineering. IEEE Trans. on Software Engineering. 26(10): 978-1005.
  2. i* Framework - Yu, E. 1995. Modeling Strategic Relationships for Process Reengineering. PhD thesis, University of Toronto.
  3. PRACTIONIST framework - Morreale, V., Bonura, S., Francaviglia, G., Centineo, F., Cossentino, M., and Gaglio, S. 2006. Goal-Oriented Development of BDI Agents: The PRACTIONIST Approach. In Proceedings of the IEEE/WIC/ACM international Conference on intelligent Agent Technology (IAT), 66-72. IEEE Computer Society.
  
* iii4 - **Motivational Statements** - The purpose of the paper, which the authors highlight in the beginning of it, is to allow a
designer to specify goals during requirements and then use those same goals throughout system development and at runtime. Through the descriptions and walkthroughs that the authors have presented, they propose to have developed a model (GMoDS) for ensuring design time goals are translatable to runtime properties of the system.


#### Improvements

1. As an example, the authors have chosen to model a WMD detection functionality of a system in the GMoDS goal model. While they convincingly depict the interaction of design time and run time subgoals of the goal, there should be an example of how orthogonal functionality goals of the system interact with each other and how that is modelled in the GMoDS model.

2. There are systems which do not have a fixed set of design time goals. Rather Rule Engines and Decision Tables map the target action with a context. Rules as such do not have any particular heirarchy or well defined relation. The authors of GMoDS can investigate if their GMoDS model can be applied or adapted to such a system

3. The authors should consider improving the depiction of the goals, subgoals and their relations in the illustrations. Consider having different notations for parent goals, sub-goals, precedents and negative triggers. These visual elements add to the understanding of the goal structure.

#### Relation to Paper One

This paper is an implementation method of the concepts proposed in Paper One. The authors of Paper One propose a model for specifying and verifying goals at runtime. This paper elaborates on a process to structure goals, sub-goals and their relations so that they maybe be easily mapped to runtime verifiable goals.