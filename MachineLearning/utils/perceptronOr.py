import pandas as pd
from utils.perceptron import Perceptron
class OrPerceptron(Perceptron):
    def __init__(self, learning_rate, epochs):
        super().__init__(learning_rate=learning_rate, epochs=epochs)

    def fit(self):
        df = pd.read_csv("../../dataset/or.csv")
        X = df.iloc[:, :-1].values
        y = df["y"]
        super().train(X, y)
