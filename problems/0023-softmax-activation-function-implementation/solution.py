import math

def softmax(scores: list[float]) -> list[float]:
    mymax = max(scores)
    softmax = [math.exp(i-mymax) for i in scores]
    softmax = [i/sum(softmax) for i in softmax]
    return softmax