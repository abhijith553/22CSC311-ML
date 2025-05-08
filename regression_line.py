from sklearn import linear_model
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X_var = []
Y_var = []

for k in range(1, 100 + 1):
    x = k + 15
    X_var.append(x + np.random.normal(loc=0.0, scale = 4.0))
    Y_var.append(x*1.5 + np.random.normal(loc=0.0, scale = 6.0))

Regr_data = pd.DataFrame(list(zip(X_var, Y_var)), columns = ["X", "Y"])
Regr_data.plot(x = "X", y = "Y", kind = "scatter", color = "black", label = "Data points")
plt.legend(loc = "upper left")
plt.show()
