from math import inf
import random


class MinimaxAlgorithm:
    def __init__(self, predict_step, black_white, d):
        self.predict_step = predict_step
        self.predicted = []
        self.black_white = black_white
        self.d = d
        self.score = 0




    def generate(self):
        self.predict_step()

    def minimax(self, position: list, depth: int, maximizing_player: bool, black_white: dict):
        if depth == 0:
            if maximizing_player:
                that_color, opponent_color = black_white['white'] + [position], black_white['black']
                return [position, len(self.predict_step())]
            else:
                that_color, opponent_color = black_white['black'] + [position], black_white['white']
                return [position, -len(self.predict_step())]

        if maximizing_player:
            max_eval = -inf
            that_color, opponent_color = black_white['white'] + [position], black_white['black']
            for child in self.predicted:
                black_white = {'white': that_color, 'black': opponent_color}
                eval = self.minimax(child, depth - 1, False, black_white)[1]
                max_eval = max(max_eval, eval)

            return [position, max_eval]
        else:
            min_eval = inf
            that_color, opponent_color = black_white['black'] + [position], black_white['white']
            for child in self.predicted:
                black_white = {'white': opponent_color, 'black': that_color}
                eval = self.minimax(child, depth - 1, True, black_white)[1]
                min_eval = min(min_eval, eval)

            return [position, min_eval]


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

