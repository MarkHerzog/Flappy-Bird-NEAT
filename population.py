from Bird import Bird
import random

class Population:
    def __init__(self):
        self.population = 100
        self.birds = [Bird() for bird in range(self.population)]
        self.dead_birds = []
        self.gen = 0
    def new(self):
        self.birds = self.dead_birds[:]
        self.gen += 1
        self.bird_fitness = [[bird.fitness, i] for bird, i in zip(self.dead_birds, range(len(self.birds)))]
        self.bird_fitness.sort(reverse=True)
        self.bird_fitness1 = self.bird_fitness[:9]
        new = []
        for gb, bb in zip(self.bird_fitness1, self.bird_fitness[:9]):
            new_bird = Bird()
            new_bird.b_i_h, new_bird.b_h_o, new_bird.b_i_h, new_bird.b_h_o = self.birds[gb[1]].child(self.birds[bb[1]])
            new.append(new_bird)
            new_bird1 = Bird()
            new_bird1.b_i_h, new_bird1.b_h_o, new_bird1.b_i_h, new_bird1.b_h_o = self.birds[gb[1]].child(self.birds[bb[1]])
            new.append(new_bird1)
            new.append(self.birds[gb[1]])
        while len(new) <= 100:
            new.append(Bird())
        self.birds = new[:]
        self.dead_birds.clear()
        return self.bird_fitness[0][0]


    def dead(self, list_):
        for dead_bird in list_:
            self.dead_birds.append(dead_bird)
            self.birds.remove(dead_bird)
