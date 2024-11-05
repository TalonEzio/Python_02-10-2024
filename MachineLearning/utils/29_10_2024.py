from utils.perceptronAnd import AndPerceptron
from utils.perceptronOr import OrPerceptron
from utils.perceptronNot import NotPerceptron
import numpy as np

if __name__ == '__main__':
    not_perceptron = NotPerceptron(learning_rate=0.001, epochs=1000)
    and_perceptron = AndPerceptron(learning_rate=0.001, epochs=1000)
    or_perceptron = OrPerceptron(learning_rate=0.001, epochs=1000)

    not_perceptron.fit()
    and_perceptron.fit()
    or_perceptron.fit()

    print("NOT Perceptron")
    print(f"w:{not_perceptron.weights} và bias:{not_perceptron.bias} ")
    print(not_perceptron.predict(np.array([[0], [1]])))  # Output: [1, 0]

    print("AND Perceptron")
    print(f"w:{and_perceptron.weights} và bias:{and_perceptron.bias} ")
    print(and_perceptron.predict(np.array([[0, 0], [0, 1], [1, 0], [1, 1]])))  # Output: [0, 0, 0, 1]

    print("OR Perceptron")
    print(f"w:{or_perceptron.weights} và bias:{or_perceptron.bias} ")
    print(or_perceptron.predict(np.array([[0, 0], [0, 1], [1, 0], [1, 1]])))  # Output: [0, 1, 1, 1]