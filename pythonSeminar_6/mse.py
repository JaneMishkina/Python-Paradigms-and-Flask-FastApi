import numpy as np
def calculate_mse(y_true, y_pred):
    n = len(y_true)
    if n != len(y_pred):
        raise ValueError ("Длины массивов должны быть одинаковыми")
    return np.square(np.subtract(y_true,y_pred)).mean()
y_true = [1, 6, 8, 7, 3]
y_pred = [1.1, 6.3, 8.1, 7.3, 56.3]
print(calculate_mse(y_true, y_pred))