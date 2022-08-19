from population import Population
from game import Game
import matplotlib.pyplot as plt

pop = Population()
game = Game()
gen =[]
max_fitness = []
plt.xlabel('Gen')
plt.ylabel('Max_fitness')
while True:
    pop.dead(game.play_frame(pop.birds, pop))
    for bird in pop.birds:
         bird.update([game.close_pillar().y2 / 10, bird.y / 10, bird.y_change / 10], game)
    if len(pop.birds) == 0:
        game.restart()
        max_fitness.append(pop.new() / 100)
        gen.append(pop.gen)
    plt.plot(gen, max_fitness, 'ko--')
