import numpy as np
from sklearn.model_selection import train_test_split

class Input:
    def __init__(self, w1,w2,w3,w4, target_type):
        self.W1 = w1
        self.W2 = w2
        self.W3 = w3
        self.W4 = w4
        self.TargetType = target_type

class TargetType:
    setosa = 0
    versicolor = 1


class Perceptron:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.W1 = np.random.randint(-5, 5)
        self.W2 = np.random.randint(-5, 5)
        self.W3 = np.random.randint(-5, 5)
        self.W4 = np.random.randint(-5, 5)

        self.Bias = np.random.rand()

    @staticmethod
    def unit_step(value):
        return 1 if value > 0 else 0

    def train(self, input_list, epochs):
        for epoch in range(epochs):
            total_error = 0

            for input_obj in input_list:
                w1 = input_obj.W1
                w2 = input_obj.W2
                w3 = input_obj.W3
                w4 = input_obj.W4

                y_true = (int)(input_obj.TargetType)

                weighted_sum = self.W1 * w1 + self.W2 * w2 + self.W3 * w3 + self.W4 * w4 + self.Bias
                y_predict = self.unit_step(weighted_sum)

                error = y_true - y_predict

                total_error += abs(error)

                if error != 0:
                    self.W1 += self.learning_rate * error * w1
                    self.W2 += self.learning_rate * error * w2
                    self.W3 += self.learning_rate * error * w3
                    self.W4 += self.learning_rate * error * w4
                    self.Bias += self.learning_rate * error

            if total_error == 0:
                print(f'lỗi về 0 tại lần lặp thứ {epoch}')
                break

    def predict(self, input: Input):

        weighted_sum = self.W1 * input.W1 + self.W2 * input.W2 + self.W3 * input.W3 + self.W4 * input.W4 + self.Bias
        return self.unit_step(weighted_sum)

    pass

    def evaluate(self, test_data):
        correct_predictions = 0
        for input_obj in test_data:
            y_true = input_obj.TargetType
            y_predict = self.predict(input_obj)
            if y_true == y_predict:
                correct_predictions += 1
        return correct_predictions / len(test_data)

def read_files(filePath):
    input_list = []
    with open(filePath, 'r') as file:
        for line in file:
            values = line.strip().split(',')

            w1, w2, w3, w4 = map(float, values[:4])
            iris_type = TargetType.setosa if values[4] == 'Iris-setosa' else TargetType.versicolor

            input_list.append(Input(w1, w2, w3, w4, iris_type))
    return input_list

def split_data(input_list):
    train_data, test_data = train_test_split(input_list, test_size=0.2, random_state=42,shuffle=True)
    return train_data, test_data

if __name__ == '__main__':

    input_list = read_files("iris-data.txt")


    train_data, test_data = split_data(input_list)

    perceptron = Perceptron(learning_rate=0.001)
    perceptron.train(train_data, epochs=1000)


    accuracy = perceptron.evaluate(test_data)
    print(f"Độ chính xác của mô hình trên tập kiểm thử: {accuracy * 100:.2f}%")


    for input in input_list:
        print(input.W1,input.W2,input.W3,input.W4,input.TargetType)

