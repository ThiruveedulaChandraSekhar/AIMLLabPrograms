import numpy as np


class McCullochPittsNeuron:
    def __init__(self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold

    def activation(self, inputs):
        weighted_sum = np.dot(inputs, self.weights)
        return 1 if weighted_sum >= self.threshold else 0


def AND_neuron(x1, x2, x3):
    weights = [1, 1, 1]
    threshold = 3
    neuron = McCullochPittsNeuron(weights, threshold)
    return neuron.activation([x1, x2, x3])


def OR_neuron(x1, x2, x3):
    weights = [1, 1, 1]
    threshold = 1
    neuron = McCullochPittsNeuron(weights, threshold)
    return neuron.activation([x1, x2, x3])


def NOR_neuron(x1, x2, x3):
    weights = [-1, -1, -1]
    threshold = 0
    neuron = McCullochPittsNeuron(weights, threshold)
    return neuron.activation([x1, x2, x3])


def NAND_neuron(x1, x2, x3):
    weights = [-1, -1, -1]
    threshold = -2
    neuron = McCullochPittsNeuron(weights, threshold)
    return neuron.activation([x1, x2, x3])


# Test the functions
inputs = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

print("AND Gate:")
for i in inputs:
    print(f"AND({i[0]}, {i[1]}, {i[2]}) = {AND_neuron(i[0], i[1], i[2])}")

print("\nOR Gate:")
for i in inputs:
    print(f"OR({i[0]}, {i[1]}, {i[2]}) = {OR_neuron(i[0], i[1], i[2])}")

print("\nNOR Gate:")
for i in inputs:
    print(f"NOR({i[0]}, {i[1]}, {i[2]}) = {NOR_neuron(i[0], i[1], i[2])}")

print("\nNAND Gate:")
for i in inputs:
    print(f"NAND({i[0]}, {i[1]}, {i[2]}) = {NAND_neuron(i[0], i[1], i[2])}")
