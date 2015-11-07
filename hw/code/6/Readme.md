### About:
The program finds a solution that maximizes Schaffer, Osyczka2 & Kursawe models using Simulated Annealing and minimizes them using Max Walk Sat algorithms.

### Output:
```
Model: Schaffer Model
Optimizer: Simulated Annealing
e0 = 1.29E-01
s0 = [-3587]

Final Solution: 
eb = 1.21E-06
sb = [12]
```

```
Model: Schaffer Model
Optimizer: Max Walk Sat
e0 = 0.5254
s0 = [-7248]
Parameters used:
maxtries=200
maxchanges=50
p=0.5
threshold=1
steps=10
Total evaluations: 49530
Final Solution: 
sb: ['-9999.00'] 
eb : 0.9998
```
```
Model: Kursawe Model
Optimizer: Simulated Annealing
e0 = 6.74E-01
s0 = [-5, 4, 1]

Final Solution: 
eb = 0.00E+00
sb = [-1, -1, -1]
```
```
Model: Kursawe Model
Optimizer: Max Walk Sat
e0 = 0.2025
s0 = [-1, -2, -3]
Parameters used:
maxtries=200
maxchanges=50
p=0.5
threshold=1
steps=10
Total evaluations: 50020
Final Solution: 
sb: ['-5.00', '-5.00', '-5.00'] 
eb : 1.0000
```

```
Model: Osyczka2 Model
Optimizer: Simulated Annealing
e0 = 8.03E-01
s0 = [2, 3, 2, 0, 2, 6]

Final Solution: 
eb = 5.48E-02
sb = [5, 1, 4, 0, 1, 5]
```

```
Model: Osyczka2 Model
Optimizer: Max Walk Sat
e0 = 0.2939
s0 = [5, 1, 4, 2, 4, 4]

Parameters used:
maxtries=200
maxchanges=50
p=0.5
threshold=1
steps=10
Total evaluations: 58204
Final Solution: 
sb: ['2.00', '4.00', '3.40', '3.60', '4.60', '9.00'] 
eb : 0.9996
```

Detailed Output can be found in output.txt


### Notations:

"!" = new best solution found

"+" = local solution better than current solution found

"." = no new solution found

"?" = solution found is worse that current
