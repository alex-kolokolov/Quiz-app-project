import random


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


