# Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function
#     -extracting equations from inputs and outputs
#     -mean square error = cost fucn (diff of point and line squared)
#     -gradient decent is efficient algo to find line of best fit (no want to interate over all m and b in y = mx + b)
#         -find lowest point of curved plane ("m" x "b" x "cost" plot)
#     -calculus: partial derivatives (find d/dx = 0 for each variable in the mean square func)

import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])


def gradient_descent(x, y):
    m_curr = b_curr = 0  # starting point for m and b, then take baby steps
    iterations = 1000  # num baby steps
    n = len(x)  # for sums
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val**2 for val in (y - y_predicted)])

        # m partial derivative (from mean square func)
        md = -(2 / n) * sum(x * (y - y_predicted))
        # b partial derivative (from mean square func)
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m:", m_curr, "b:", b_curr, "md:", md, "bd:", bd, "cost:", cost)


gradient_descent(x, y)
