from population import Population
from game import Game

pop = Population()
game = Game()
while True:
    pop.dead(game.play_frame(pop.birds, pop))
    for bird in pop.birds:
         bird.update([game.close_pillar().y2 / 10, bird.y / 10, bird.y_change / 10], game)
    if len(pop.birds) == 0:
        game.restart()
        pop.new()
