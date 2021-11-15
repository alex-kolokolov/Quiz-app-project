from math import inf
import random


class MinimaxAlgorithm:
    def __init__(self, predict_step, black_white, d):
        self.predict_step = predict_step
        self.predicted = []
        self.black_white = black_white
        self.d = d
        self.score = 0


class RandomBot:

    def __init__(self):
        self.predicted = []
        self.availbale_steps = dict()

    def get_values(self, predicted: list, available_steps: dict):
        self.predicted = predicted
        self.availbale_steps = available_steps

    def calculate(self):
        if len(self.predicted) > 0:
            return random.choice(self.predicted)
