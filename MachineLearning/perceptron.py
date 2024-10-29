import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

class Input:
    def __init__(self, x, y, target_type):
        self.X = x
        self.Y = y
        self.TargetType = target_type

    @staticmethod
    def generate_linearly_separable_data(input_count, range_val, scale):
        data = []
        a = random.uniform(-range_val, range_val)
        b = random.uniform(-range_val, range_val)

        for _ in range(input_count):
            x = random.randint(-range_val * scale, range_val * scale)
            y = random.randint(-range_val * scale, range_val * scale)

            label = TargetType.Yellow if y > a * x + b else TargetType.Blue
            data.append(Input(x, y, label))

        return data, a, b


class TargetType:
    Blue = 0
    Yellow = 1


class Perceptron:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.W1 = np.random.randint(-5, 5)
        self.W2 = np.random.randint(-5, 5)

        self.Bias = np.random.rand()

        # Cache random value
        self.W1Default = self.W1
        self.W2Default = self.W2

    @staticmethod
    def unit_step(value):
        return 1 if value > 0 else 0

    def train(self, input_list, epochs):
        for epoch in range(epochs):
            total_error = 0
            for input_obj in input_list:
                x1 = input_obj.X
                x2 = input_obj.Y
                y_true = input_obj.TargetType

                weighted_sum = self.W1 * x1 + self.W2 * x2 + self.Bias
                y_predict = self.unit_step(weighted_sum)

                error = y_true - y_predict
                total_error += abs(error)

                if error != 0:
                    self.W1 += self.learning_rate * error * x1
                    self.W2 += self.learning_rate * error * x2
                    self.Bias += self.learning_rate * error

            if total_error == 0:
                break

    def predict(self, x1, x2):
        weighted_sum = self.W1 * x1 + self.W2 * x2 + self.Bias
        result = self.unit_step(weighted_sum)
        return TargetType.Yellow if result == 1 else TargetType.Blue

    def evaluate(self, test_data):
        correct_predictions = 0
        for input_obj in test_data:
            prediction = self.predict(input_obj.X, input_obj.Y)
            if prediction == input_obj.TargetType:
                correct_predictions += 1
        accuracy = correct_predictions / len(test_data)
        return accuracy


def plot_data_and_decision_boundary(data, perceptron, a, b):
    square_points = [(d.X, d.Y) for d in data if d.TargetType == TargetType.Blue]
    circle_points = [(d.X, d.Y) for d in data if d.TargetType == TargetType.Yellow]

    plt.scatter([x[0] for x in square_points], [x[1] for x in square_points], color='blue', label='Blue')
    plt.scatter([x[0] for x in circle_points], [x[1] for x in circle_points], color='yellow', label='Yellow')

    x_vals = range(-50, 50)
    y_vals = [a * x + b for x in x_vals]
    plt.plot(x_vals, y_vals, label='Đường thẳng sinh ra dữ liệu', color='red')


    x_vals = range(-50, 50)
    y_vals = [perceptron.W1Default * x + perceptron.W2Default for x in x_vals]
    plt.plot(x_vals, y_vals, label='Đường thẳng phân tách ban đầu', color='green')


    if perceptron.W2 != 0:
        y_perceptron = [-(perceptron.W1 * x + perceptron.Bias) / perceptron.W2 for x in x_vals]
        plt.plot(x_vals, y_perceptron, label='Đường phân chia Perceptron', linestyle='--', color='purple')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Phân bố điểm và đường phân chia của Perceptron')
    plt.legend()
    plt.grid(True)
    plt.show()


# Main program
if __name__ == "__main__":
    input_count = 1000
    linear_separable_data, a, b = Input.generate_linearly_separable_data(input_count, 20, 20)

    train_data, test_data = train_test_split(linear_separable_data, test_size=0.2)

    perceptron = Perceptron(learning_rate=0.01)
    perceptron.train(train_data, epochs=1000)

    accuracy = perceptron.evaluate(test_data)
    print(f"Độ chính xác của mô hình trên tập kiểm thử: {accuracy * 100:.2f}%")

    plot_data_and_decision_boundary(linear_separable_data, perceptron, a, b)
