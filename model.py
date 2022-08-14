import random
from game import Game
class Bird:
    def __init__(self):
        self.weights = [r for r in [random.uniform(-0.5, 0.5) for i in range(3)]]
        self.y = 200
        self.y_change = 0
        self.fitness = 0
    def predict(self, list_inputs):
        weights = sum([w * i for w, i in zip(self.weights, list_inputs)])
        return weights
    def update(self, list_inputs, game):
        pred = self.predict(list_inputs)
        if round(pred) == 1: self.y_change = -3.5
        self.y_change += 0.1
        self.y += self.y_change
        self.fitness += game.pass_pillar()
