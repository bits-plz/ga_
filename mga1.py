#author => MOHIT KUMAR SINGH
import numpy as np
from ypstruct import structure
import ga
import math
from functools import lru_cache
from evaluate import evalexp


# test function ALL FUNCTIONS LIVE HERE you can add more functions as you go like here i have rastrigin and the sphere function(it's what i called it)
def sphere(func,x):
    global q
    sumr=0
    for item in x:
        sumr+=math.pow(item,float(q))
    return sumr


def rastrigin(func,x):
    sumr=20.00
    for item in x:
        sumr+=math.pow(item,2)-10*math.cos(2*math.pi*item)
    return sumr



def func_eval(func,x):
    expr=evalexp()
    sumr=0.00
    rt=func
    for item in x:
        v_expr=rt.replace("j",str(item))
        sumr+=expr.evalexpr(v_expr)
        rt=func
    return sumr

q=2
@lru_cache
def m_ga1(func,nvar,varmin,varmax,maxit,npop,optimization="min",gamma=0.1,mu=0.1,sigma=0.1,beta=1,pc=1):
    global q
    problem = structure()
    #here in the elifs you can add the make the func what you added above
    if "x^" in func:
        p,q=func.split("^")
        problem.costfunc=sphere
    elif func=='@rastrigin':#it's your choice what you add here like i enter func name as @rastrigin and the function called is rastrigin
        problem.costfunc=rastrigin
    else:
        problem.costfunc=func_eval
    problem.func_expr=func
    problem.nvar = nvar
    varmin=varmin.split(',')
    varmax=varmax.split(',')
    problem.varmin = []
    problem.varmax=[]
    for item in varmin:
        problem.varmin.append(float(item))
    for item in varmax:
        problem.varmax.append(float(item))


    params = structure()
    params.maxit = maxit#the max iterations required
    params.npop = npop#the initial population 
    params.pc = pc
    params.gamma = gamma
    params.mu = mu#mutation rate
    params.sigma = sigma
    params.beta=beta
    params.optimization=optimization
    # run ga    
    result = ga.run_ga(problem, params)
    std=np.std([x['cost'] for x in result.pop])
    print(f"following are the last offsprings {result.bestsol['position']}")
    print(f"the cost is {result.bestsol['cost']}")
    return result,std,result.bestsol['position']
