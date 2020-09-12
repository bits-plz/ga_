# ga_
simple GUI implementing genetic algorithms
>The algo is taken from youtube channel "yarpiz"
This app uses tkinter for gui and matplotlib for plotting the cost vs generation curve

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


# Errors involved
  wherever i could find meaningful Errors i have tried to show an error screen but certain errors such as the error involved with slow pure-
  python sequencematcher can be resolved by installing python-Levenshtein package which is involved with fuzzywuzzy in the string genetic 
  algorithm plus since this hasn't been tested for all the inputs there could be more errors
