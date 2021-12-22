import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def premium_prediction(age):

    X = pd.read_csv("X_train.csv")
    y = pd.read_csv("Y_train.csv")

    # plt.scatter(X,y)
    # plt.xlabel("Age")
    # plt.ylabel("Premium")
    # plt.show()

    model = LinearRegression()

    model.fit(X, y)

    X_test = np.array(age)
    X_test = X_test.reshape(1, -1)

    return model.predict(X_test)
