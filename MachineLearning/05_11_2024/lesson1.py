from typing import List
import pandas as pd
from pandas.core.computation.expressions import evaluate


class Input:
    def __init__(self, x1, x2, y):
        self.X1 = x1
        self.X2 = x2
        self.Y = y


class Perceptron:
    def __init__(self, w1, w2, bias, learning_rate):
        self.W1 = w1
        self.W2 = w2
        self.Bias = bias
        self.LearningRate = learning_rate

        # Cache value
        self.W1Default = self.W1
        self.W2Default = self.W2

    @staticmethod
    def unit_step(value):
        return 1 if value > 0 else 0

    def train(self, input_list: List[Input], epochs: int):
        for epoch in range(epochs):

            total_error = 0

            for input_obj in input_list:
                x1 = input_obj.X1
                x2 = input_obj.X2
                y_true = input_obj.Y

                weighted_sum = self.W1 * x1 + self.W2 * x2 + self.Bias
                y_predict = self.unit_step(weighted_sum)

                error = y_true - y_predict
                total_error += abs(error)

                if error != 0:
                    self.W1 += self.LearningRate * error * x1
                    self.W2 += self.LearningRate * error * x2
                    self.Bias += self.LearningRate * error

            if total_error == 0:
                break

    def predict(self, input: Input):
        weighted_sum = self.W1 * input.X1 + self.W2 * input.X2 + self.Bias
        result = self.unit_step(weighted_sum)
        return 1 if result == 1 else 0

    def evaluate(self, test_data: List[Input]):
        correct_predictions = 0
        for input_obj in test_data:
            prediction = self.predict(input_obj)
            if prediction == input_obj.Y:
                correct_predictions += 1
        accuracy = correct_predictions / len(test_data)
        return accuracy

if __name__ == '__main__':
    csvPath = './lesson1.csv'

    data_frame = pd.read_csv(csvPath)

    input_list = []
    for index, row in data_frame.iterrows():
        x1 = row['X1']
        x2 = row['X2']
        y = row['Y']
        input_list.append(Input(x1, x2, y))

    for input_obj in input_list:
        print(f'X1: {input_obj.X1}, X2: {input_obj.X2}, Y: {input_obj.Y}')

    perceptron = Perceptron(w1=0.5, w2=0.5, bias=-0.5, learning_rate=0.1)


    perceptron.train(input_list, epochs=1000)

    evaluate = perceptron.evaluate(input_list)

    print(f'{evaluate * 100}%')

