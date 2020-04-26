import random
#Todo: change the population generation, right now each individual 
#is one number try to make each individual a list or dictionary of numbers  
randomlist = random.sample(range(10,30),5)
print(randomlist)
pop = init_pop(pop)
gen = select_mating(pop)
pop = []
def init_pop(pop):
    new_pop = [a for a in pop]
    return new_pop

def select_mating(pop):
    #Here can add elitism or other methods of selecting the ind
    generation = [a for a in pop if a > 10]
    return generation

def crossover(gen, prob = .5):
    childs = []
    for x in gen:
        for y in gen:
            if y is not x and random.randint(0,10) < prob*10:
                continue#do crossover here

def mutations(children, prob=0.5):
    #Do this per gene per individual
    childs =[random.randint(10,30) if prob*10 > random.randint(0,10) else a 
            for a in children if prob*10 > random.randint(0,10)]
    return childs

#Test population score and report, repeat steps?
                