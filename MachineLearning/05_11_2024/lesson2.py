from typing import List
import pandas as pd
from matplotlib import pyplot as plt


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

        self.W1Default = self.W1
        self.W2Default = self.W1

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
        return self.unit_step(weighted_sum)

    def evaluate(self, test_data: List[Input]):
        correct_predictions = sum(1 for input_obj in test_data if self.predict(input_obj) == input_obj.Y)
        accuracy = correct_predictions / len(test_data)
        return accuracy

    def get_line_equation(self):
        return -self.Bias, self.W1, self.W2


if __name__ == '__main__':
    csv_path = './lesson2.csv'
    data_frame = pd.read_csv(csv_path)

    input_list = [Input(row['x1'], row['x2'], row['y']) for _, row in data_frame.iterrows()]

    for input_obj in input_list:
        print(f'X1: {input_obj.X1}, X2: {input_obj.X2}, Y: {input_obj.Y}')

    perceptron = Perceptron(w1=1, w2=2, bias=0.1, learning_rate=0.1)

    perceptron.train(input_list, epochs=1000)

    evaluate = perceptron.evaluate(input_list)

    print(f'Accuracy: {evaluate * 100:.2f}%')

    print(f'Weights after training: W1: {perceptron.W1}, W2: {perceptron.W2}, Bias: {perceptron.Bias}')

    w0, w1, w2 = perceptron.get_line_equation()
    print(f'Line equation: {w0} * (-1) + {w1} * x1 + {w2} * x2 = 0')

    colors = ['blue' if input_obj.Y == 0 else 'red' for input_obj in input_list]
    plt.scatter([input_obj.X1 for input_obj in input_list], [input_obj.X2 for input_obj in input_list], c=colors)

    x_vals = range(0, 10)
    y_vals_default = [perceptron.W1Default * x + perceptron.W1Default for x in x_vals]
    plt.plot(x_vals, y_vals_default, label='Đường thẳng ban đầu', color='green')

    x_vals = range(0, 10)
    y_vals_trained = [(-w0 + w1 * x) / w2 for x in x_vals]  # Giải phương trình cho x2
    plt.plot(x_vals, y_vals_trained, label='Đường thẳng sau train', color='purple')



    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.grid(True)
    plt.legend('Test')
    plt.show()
