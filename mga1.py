#author => MOHIT KUMAR SINGH
import numpy as np
from ypstruct import structure
import ga
import math
from functools import lru_cache
from evaluate import evalexp
from datetime import datetime
import threading
res=[]
def wrapper(func,args,res):
    res.append(func(*args))

# test function ALL FUNCTIONS LIVE HERE you can add more functions as you go like here i have rastrigin and the sphere function(it's what i called it)
def sphere(func,x):
    global q
    sumr=0
    for item in x:
        sumr+=math.pow(item,float(q))
    return sumr


def rastrigin(func,x):
    sumr=len(x)*10
    for item in x:
        sumr+=math.pow(item,2)-10*math.cos(2*math.pi*item)
    return sumr

def ackley_path(func,x):
    n=len(x)
    rp=list(map(lambda y: y**2,x))
    sumsq=sum(rp)
    sumcs=0
    for item in x:
        sumcs+=math.cos(2*math.pi*item)
    return -20*math.exp(-0.2*math.sqrt(sumsq)/n)-math.exp(sumcs/n)+20+math.exp(1)

def griewangk(func,x):
    sumsq=0
    prod=1
    for idx,item in enumerate(x):
        sumsq+=math.pow(item,2)/4000
        prod=prod*(math.cos(item/math.sqrt(idx+1)))
    return sumsq+prod+1

def schwefel(func,x):
    res=0
    for item in x:
        res+=item*math.sin(math.sqrt(abs(item)))
    return res




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
def m_ga1(func,nvar,varmin,varmax,maxit,npop,optimization,thread_it,selection_type,x_type,gamma=0.1,mu=0.1,sigma=0.1,beta=1,pc=1):
    if(len(res)>0):
        res.clear()
    in_it=datetime.now()
    global q
    problem = structure()
    #here in the elifs you can add the make the func what you added above
    if "x^" in func:
        p,q=func.split("^")
        problem.costfunc=sphere
    elif func=='@rastrigin':#it's your choice what you add here like i enter func name as @rastrigin and the function called is rastrigin
        problem.costfunc=rastrigin
    elif func =="@ackley":
        problem.costfunc=ackley_path
    elif func=="@schwefel":
        problem.costfunc=schwefel
    elif func=="@griewangk":
        problem.costfunc=griewangk
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
    params.selection_type=selection_type
    params.x_type=x_type
    # run ga    
    if(thread_it=="Yes"):
        t=threading.Thread(target=wrapper,args=(ga.run_ga,(problem,params),res))
        t.start()
        while(len(res)==0):
            pass
        t.join()
        print(res)
        result = res[0]
    else:
        result=ga.run_ga(problem,params)
    std=np.std([x['cost'] for x in result.pop])
    fin_time=datetime.now()
    print(f"execution time is {fin_time-in_it}")
    print(f"following are the last offsprings {result.bestsol['position']}")
    print(f"the cost is {result.bestsol['cost']}")
    return result,std,result.bestsol['position']


def m_ga2(func,nvar,varmin,varmax,maxit,npop,optimization,thread_it,selection_type,gamma=0.1,mu=0.1,sigma=0.1,beta=1,pc=1):
    if(len(res)>0):
        res.clear()
    in_it=datetime.now()
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
    params.selection_type=selection_type
    params.x_type="hc/ic"
    # run ga    
    if(thread_it=="Yes"):
        t=threading.Thread(target=wrapper,args=(ga.run_ga,(problem,params),res))
        t.start()
        while(len(res)==0):
            pass
        t.join()
        print(res)
        result = res[0]
    else:
        result=ga.run_ga(problem,params)
    std=np.std([x['cost'] for x in result.pop])
    fin_time=datetime.now()
    print(f"execution time is {fin_time-in_it}")
    print(f"following are the last offsprings {result.bestsol['position']}")
    print(f"the cost is {result.bestsol['cost']}")
    return result,std,result.bestsol['position']

