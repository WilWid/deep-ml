import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    
    probabilities = []
    error = []

    for i in range(len(features)):
        currfeat = features[i]
        tmp = weights[0] * currfeat[0] + weights[1] * currfeat[1] + bias

        probability = 1 / (1 + math.exp(-tmp))
        probabilities.append(round(probability,4))
        error.append(round((probability - labels[i]) ** 2,4))
    mse = [math.sqrt(i ** 2) for i in error]
    mse = round(sum(mse) / len(mse),4)

    return probabilities, mse