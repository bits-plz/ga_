# ga_
simple GUI implementing genetic algorithms

>This app uses tkinter for gui and matplotlib for plotting the cost vs generation curve hats off to yarpiz visit him at https://www.youtube.com/channel/UCz6Q1WpIhQDD0Wvb7RlL9Sw

## Modules
* ypstruct
* fuzzywuzzy
* matplotlib
* tkinter
* simple-eval

## tweaks
  * for example the mutation rate ("mu") is in between 0 and 1 and by default is 0.1
  * the beta value is used to find the selection pressure that is used to find probabilities for roullette selection, the beta value is also 
   between 0 and 1
  * gamma value is used in the crossover function and it also lies between 0 and 1, the gamma value is used to perform crossover over
   the population
  * probability count is used for determining how much the children we want to be generated 

# the explanation
 ## Following is the brief understanding of the algorithms involved 
   * the population is generated from max_population 
   * the crossover is performed between the population in order to get offsprings
   * the mutation is performed which is essential in order to further improve the yield
   * the above steps are repeated for #gen times
   * the results are shown as a graph and bestcost as well as standard deviation of the various generation bescost are shown
            on the panel below the "BEGIN" button and the last offsprings are also shown in the respected Label and also the entire best solution
            is printed on console
# Algo
The very idea behind the genetic algorithms are that we will look for the solution in entire search space but efficiently and the stress should be on how we will be improving the children solutions as the time passes.
We shall discuss the steps one by one for both the programs included in the application.
First step is obvious that we will generate random parents in the search space, the following two lines demonstrate the generation of the parents in ga_.py and ga.py .
## init population
1.
```
self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
```
2.
```
.pop[i].position = np.random.uniform(varmin, varmax, nvar)
```


The above generate the parents in thier respective programs, let us discuss both of them, the first one is used in ga_.py and is using the random choice function which selects the alphabets according to given list. The second one generates “nvar” values in range of their corresponding bounds i.e [varmin,varmax]
The very next step is to determine what is their corresponding fitness status.
In string matching we just compare the string and determine how good is this string in comparison to the target string.
## costfunction

1.
```
agent.fitness = fuzz.ratio(agent.string, in_str)
```

2.
```
pop[i].cost = costfunc(func_expr,pop[i].position)
```
As we can see that in the first program fitness of a child is calculated by fuzz.ratio(), which takes in two parameters and does exactly what was discussed. The second one is more straight-forward as it just assigns the cost value to be the evaluation of the function for that set of variables. 


## Crossover-step
1.
```
    split = random.randint(0, in_str_len)
    child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
    child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]
```

2.
```
    c1 = p1.deepcopy()
    c2 = p1.deepcopy()
    alfa = np.random.uniform(-gamma, 1 + gamma, *c1.position.shape)
    c1.position = alfa * p1.position + (1 - alfa) * p2.position
    c2.positon = alfa * p2.position + (1 - alfa) * p2.position
 ```

The above steps are used to perform the crossover in selected parents, in the first one what we do is we split the parent strings and then perform the corresponding operation.In the later case it is not that obvious here we first make deepcopies , in fact in the second program in order to separate entities we have to perform deepcopies .The value of alfa is determining where exactly to perform the crossover.It’s actually a ndarray of values as np.random.uniform(a1,a2,s) returns a list of size -> “s”.
It can also return a scalar if size is 1. More importantly it follows uniform distribution.Then the next steps simply perform crossover as suppose value of 1st  variable is 10 and  2nd is 15 and suppose alpha for this comes out to be 0.8 (say) then the new child member generated is 
0.8* 10+0.2* 15=11 and second child is 0.8* 15+0.2* 10=14
simply and this is performed as many times as the corresponding child vars.

## Mutation steps

1.
```
    for agent in agents:
        for idx, param in enumerate(agent.string):
            if random.uniform(0.0, 1.0) <= 0.1:
                agent.string = agent.string[0:idx] + random.choice(string.ascii_letters) + agent.string[idx + 1:in_str_len]
                
  ```
2.
```
    y = x.deepcopy()
    flag = np.random.rand(* x.position.shape) <= mu
    ind = np.argwhere(flag)
    y.position[ind] += sigma * np.random.randn(* ind.shape)
    
 ```
Now let us analyse the mutation steps, this step plays important role in further improving the quality of children or it may be not doing so anyways it will be handled in the selection steps because mutation although necessary might not always lead to further improvement.
The first program uses again the random choice for selecting a random letter in between the string. Suppose string is “harsypotter” suppose idx is 3 therefore if say it also happens that random.uniform(0,1) returned in val>0.1 but this time it satisfied the condition therefore the next steps must be performed therefore operation is “har”+”r”+”ypotter”( the random choice may result in returning “r”) which results in the string being “harrypotter”.
In the second program we can see a new parameter being used that is “mu” which is 0.1 by default in both programs. 
Suppose x is [0.4,0.2] and flag came out to be [True,False] therefore the
y[0] = y[0]+0.1* 0.79193536                                            (say because it’s random therefore this is just to show)
y[0] =  0.47193536
And this mutant is returned.

Selection Steps.
1.
```
    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
    agents = agents[:int(0.2 * len(agents))]           #(first 20%)
```

2.
```
        if flag=="min":
            pop = sorted(pop, key=lambda x: x.cost)
        else:
            pop=sorted(pop,key=lambda x:x.cost,reverse=True)
        pop = pop[0:maxit]
```


This step is performed after crossover and mutation , here we simply sort the population and then perform a cutoff of all the population that doesn’t satisfy the criterion.
In the second one we need to select the ones according to the type of optimization which is to be specified by the user.

# Errors involved
  wherever i could find meaningful Errors i have tried to show an error screen but certain errors such as the error involved with slow pure-
  python sequencematcher can be resolved by installing python-Levenshtein package which is involved with fuzzywuzzy in the string genetic 
  algorithm plus since this hasn't been tested for all the inputs there could be more errors
