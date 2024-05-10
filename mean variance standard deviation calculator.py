import numpy as np


def calculate(data):

    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(data).reshape(3, 3)

    result = {
        'mean': [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array).tolist()],
        'variance': [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array).tolist()],
        'standard deviation': [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array).tolist()],
        'max': [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array).tolist()],
        'min': [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array).tolist()],
        'sum': [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array).tolist()]
    }

    for key, value in result.items():
        result[key] = [np.asarray(sublist).tolist() for sublist in value]
    return result


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(calculate(data))
