# Perceptron for AND Gate(023-352)

inputs = [(0,0), (0,1), (1,0), (1,1)]
targets = [0, 0, 0, 1]

w1 = 0
w2 = 0
b = 0

learning_rate = 1

for epoch in range(10):
    for i in range(len(inputs)):
        x1, x2 = inputs[i]
        target = targets[i]

        y = w1*x1 + w2*x2 + b
        
        if y >= 0:
            output = 1
        else:
            output = 0

        error = target - output
        
        w1 = w1 + learning_rate * error * x1
        w2 = w2 + learning_rate * error * x2
        b = b + learning_rate * error

print("Final Weights:", w1, w2)
print("Final Bias:", b)

for x1, x2 in inputs:
    y = w1*x1 + w2*x2 + b
    if y >= 0:
        print(x1, x2, "→ 1")
    else:
        print(x1, x2, "→ 0")
