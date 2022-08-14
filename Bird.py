import random


class Bird:
    def __init__(self):
        self.w_i_h = [[random.random() - 0.5, random.random() - 0.5, random.random() - 0.5],
                      [random.random() - 0.5, random.random() - 0.5, random.random() - 0.5],
                      [random.random() - 0.5, random.random() - 0.5, random.random() - 0.5],
                      [random.random() - 0.5, random.random() - 0.5, random.random() - 0.5],
                      [random.random() - 0.5, random.random() - 0.5, random.random() - 0.5]]
        self.w_h_o = [[random.random() - 0.5, random.random() - 0.5,
                       random.random() - 0.5, random.random() - 0.5, random.random() - 0.5]]
        self.b_i_h = [1, 3, 1, -0.4, 0.2]
        self.b_h_o = [0.1, -0.2]
        self.y = 250
        self.y_change = 0
        self.fitness = 0
        
    def child(self, bird):
        weights_h = [[ba if random.randint(0, 1) == 0 else bb for ba, bb in zip(b1, b2)]
                       for b1, b2 in zip(bird.w_i_h, self.w_i_h)]
        weight_o = [[ba if random.randint(0, 1) == 0 else bb for ba, bb in zip(b1, b2)]
                    for b1, b2 in zip(bird.w_h_o, self.w_h_o)]
        bias_h = [b1 if random.randint(0, 1) == 0 else b2 for b1, b2 in zip(self.b_i_h, bird.b_i_h)]
        bias_o = [b1 if random.randint(0, 1) == 0 else b2 for b1, b2 in zip(self.b_h_o, bird.b_h_o)]
        return weights_h, weight_o, bias_h, bias_o

    def predict(self, inputs):
        pred_h = [sum([w * i for w, i in zip(lw, inputs)]) + b for lw, b in zip(self.w_i_h, self.b_i_h)]
        act_h = [max(0, p) for p in pred_h]
        pred_o = [sum([w * i for w, i in zip(lw, act_h)]) + b for lw, b in zip(self.w_h_o, self.b_h_o)]
        return 0 if round(pred_o[0]) < 1 else 1

    def update(self, inputs, game):
        pred = self.predict(inputs)
        if pred == 1: self.y_change = -3.5
        self.y_change += 0.1
        self.y += self.y_change
        self.fitness += game.pass_pillar()