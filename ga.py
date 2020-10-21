#author => MOHIT KUMAR SINGH
import matplotlib.pyplot as plt
import numpy as np
import math
from fuzzywuzzy import fuzz
import string
import random
from datetime import datetime



class Agent:
    def __init__(self, length):
        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.fitness = -1

    def __str__(self):
        return 'String  ' + str(self.string) + '  Fitness ' + str(self.fitness)

Fitness = []
string_file=""
count=1
def gastr(in_str,in_str_len,population,generations,k):
    initial_time=datetime.now()
    global count,string_file,Fitness
    Fitness.clear()
    string_file=""
    agents = init_agents(population, in_str_len)
    for gen in range(generations):
        agents = fitness(agents,in_str)
        agents = selection(agents)
        agents = crossover(agents,population,in_str_len)
        agents = mutation(agents,in_str_len)
        
        if (any(agent.fitness >= k for agent in agents)):
            final_time=datetime.now()
            print(f"executed in {final_time-initial_time}")
            figure = plt.figure(figsize=(6, 4))
            plt.plot(range(len(Fitness)), Fitness)
            plt.xlabel('Generations')
            plt.ylabel('Fitness')
            plt.show()
            print('Threshold met')
            st=open("Results/string/res.txt","w")
            count+=1
            string_file+=f"\n-----------------------------{count} run----------------------------\n"
            st.write(string_file)
            st.close()
            break
        if (not any(agent.fitness >= k for agent in agents) and len(Fitness)==generations):
            print("threshold couldn't be reached")
            return "threshold couldn't be reached"

def init_agents(population, length):
    return [Agent(length) for _ in range(population)]


def fitness(agents,in_str):
    for agent in agents:
        agent.fitness = fuzz.ratio(agent.string, in_str)
    return agents


def selection(agents):
    global string_file,Fitness
    fp = []
    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
    agents = agents[:int(0.2 * len(agents))]
    for item in agents:
        fp.append(item.fitness)
        string_file+=str(item)+"\n"
    Fitness.append(math.sqrt(np.mean(np.square(fp))))
    return agents


def crossover(agents,population,in_str_len):
    offspring = []
    for _ in range(int((population - len(agents)) / 2)):
        parent1 = random.choice(agents)
        parent2 = random.choice(agents)
        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)
        split = random.randint(0, in_str_len)
        child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
        child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]
        offspring.append(child1)
        offspring.append(child2)
    agents.extend(offspring)
    return agents


def mutation(agents,in_str_len):                  
    for agent in agents:
        for idx, param in enumerate(agent.string):
            if random.uniform(0.0, 1.0) <= 0.1:
                agent.string = agent.string[0:idx] + random.choice(string.ascii_letters) + agent.string[idx + 1:in_str_len]
    return agents


