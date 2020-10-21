#author => MOHIT KUMAR SINGH
from ypstruct import structure
import numpy as np


def run_ga(problem, params):
    # problem
    func_expr=problem.func_expr
    costfunc = problem.costfunc
    nvar = problem.nvar
    varmin = problem.varmin
    varmax = problem.varmax
    # params
    maxit = params.maxit
    npop = params.npop
    gamma = params.gamma
    mu = params.mu
    sigma = params.sigma
    beta = params.beta
    flag=params.optimization
    selection_type=params.selection_type
    xtype=params.x_type
    # empty individual template
    empty_ind = structure()
    empty_ind.position = None
    empty_ind.cost = None

    # bestsolution
    best_sol = empty_ind.deepcopy()
    if(flag=="min"):
        best_sol.cost = np.inf
    else:
        best_sol.cost= -np.inf
    pc = float(params.pc)
    nc = int(np.round(pc*maxit/2)*2)
    # population init
    pop = empty_ind.repeat(npop)
    for i in range(0, npop):
        pop[i].position = np.random.uniform(varmin, varmax, nvar)
        pop[i].cost = costfunc(func_expr,pop[i].position)
        try:
            if(flag=="min"):
                if (pop[i].cost < best_sol.cost):
                    best_sol = pop[i].deepcopy()
            else:
                if(pop[i].cost>best_sol.cost):
                    best_sol=pop[i].deepcopy()
        except Exception as e:
            raise(e)
    # best cost
    bestcost = np.empty(maxit)
    if selection_type=="Tournament"or selection_type=="Elitism":
            if flag=="min":
                pop = sorted(pop, key=lambda x: x.cost)
            else:
                pop=sorted(pop,key=lambda x:x.cost,reverse=True)

    # main loop
    for it in range(maxit):
        popc = []
        costs = np.array([x.cost for x in pop])
        avg_cost = np.mean(costs)
        if avg_cost != 0:
            costs = costs / avg_cost
        probs = np.exp(-beta * costs)
        for _ in range(nc // 2):  # number of childrens we want
            if(selection_type=="Random"):
                q = np.random.permutation(npop)
                p1 = pop[q[0]]
                p2 = pop[q[1]]
                p3 = pop[q[1]]
            elif(selection_type=="Tournament"):
                q_all=np.random.randint(0,npop)
                p1=pop[0]
                p2=pop[q_all]
                p2=pop[np.random.randint(0,npop)]
            elif selection_type=="Elitism":
                p1=pop[np.random.randint(0,int(npop*0.1))]
                p2=pop[np.random.randint(0,int(npop*0.1))]
                p2=pop[np.random.randint(0,int(npop*0.1))]
            else:
                p1=pop[roullete(probs)]
                p2=pop[roullete(probs)]
                p3=pop[roullete(probs)]
            #crossover
            c1, c2 = crossover(p1, p2, p3,xtype,gamma)
            # mutation
            c1 = mutate(c1, mu, sigma)
            c2 = mutate(c2, mu, sigma)

            # bounds to the positions
            apply_bound(c1, varmin, varmax)
            apply_bound(c2, varmin, varmax)
            c1.cost = costfunc(func_expr,c1.position)
            c2.cost=costfunc(func_expr,c2.position)
            if flag=="min":
                if c1.cost < best_sol.cost:
                    best_sol = c1.deepcopy()
                if c2.cost < best_sol.cost:
                    best_sol = c2.deepcopy()
            else:
                if c1.cost > best_sol.cost:
                    best_sol = c1.deepcopy()
                if c2.cost > best_sol.cost:
                    best_sol = c2.deepcopy()
            popc.append(c1)
            popc.append(c2)

        pop += popc
        if flag=="min":
            pop = sorted(pop, key=lambda x: x.cost)
        else:
            pop=sorted(pop,key=lambda x:x.cost,reverse=True)
        pop = pop[0:maxit]
        bestcost[it] = best_sol.cost

    out = structure()
    out.pop = pop
    out.bestsol = best_sol
    out.bestcost = bestcost
    out_file=open("Results/math/res.txt","wt")
    out_file.write(f"best soln {best_sol} ,best cost = {bestcost}")
    out_file.close()
    return out


def crossover(p1, p2,p3, xtype,gamma=0.1):
    alfa = np.random.uniform(-gamma, 1 + gamma, *p1.position.shape)
    c1=p1.deepcopy()
    c2=p2.deepcopy()
    if xtype=="hc/ic":
        c1.position = alfa * p1.position + (1 - alfa) * p2.position
        c2.positon = alfa * p2.position + (1 - alfa) * p2.position
    if xtype=="Three parent":
        c3=p3.deepcopy()
        c1.position=(alfa/3)*p1.position+(alfa/3)*p2.position+(alfa/3)*p3.position
        c2.position=(alfa/3)*p1.position+(alfa/3)*p2.position+(alfa/3)*p3.position
    return c1,c2



def mutate(x, mu, sigma):
    y = x.deepcopy()
    flag = np.random.rand(*x.position.shape) <= mu
    ind = np.argwhere(flag)
    y.position[ind] += sigma * np.random.randn(*ind.shape)
    return y


def apply_bound(x, varmin, varmax):
    x.position = np.maximum(x.position, varmin)
    x.position = np.minimum(x.position, varmax)


def roullete(p):
    c = np.cumsum(p)
    r = sum(p)*np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]
