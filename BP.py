import numpy as np
import math
import random

x = np.mat([[0, 0], [1, 0], [0, 1], [-1, 0], [1, -1]])
target = [1, 1, 0, 0, 0]

def BP():
    cnt = 0
    a = 1
    w1 = random.random()
    w2 = random.random()
    w3 = random.random()
    w4 = random.random()
    w5 = random.random()
    w6 = random.random()
    b1 = random.random()
    b2 = random.random()

    while cnt < 1000:
        cnt += 1
        d1 = d2 = d3 = d4 = d5 = d6 = tb1 = tb2 = 0
        for i in range(5):
            neth1 = w1 * x[i, 0] + w3 * x[i, 1] + b1
            neth2 = w2 * x[i, 0] + w4 * x[i, 1] + b1
            outh1 = 1 / (1 + math.exp(-neth1))
            outh2 = 1 / (1 + math.exp(-neth2))
            neto1 = w5 * outh1 + w6 * outh2 + b2
            out = 1 / (1 + math.exp(-neto1))
            print('%d : %.2f' % (i+1, out))
            d5 += -(target[i] - out) * out * (1 - out) * outh1
            d6 += -(target[i] - out) * out * (1 - out) * outh2
            d1 += -(target[i] - out) * out * (1 - out) * w5 * outh1 * (1 - outh1) * x[i, 0]
            d2 += -(target[i] - out) * out * (1 - out) * w6 * outh2 * (1 - outh2) * x[i, 0]
            d3 += -(target[i] - out) * out * (1 - out) * w5 * outh1 * (1 - outh1) * x[i, 1]
            d4 += -(target[i] - out) * out * (1 - out) * w6 * outh2 * (1 - outh2) * x[i, 1]
            tb2 += -(target[i] - out) * out * (1 - out)
            tb1 += -(target[i] - out) * out * (1 - out) * (w5 * outh1 * (1 - outh1) + w6 * outh2 * (1 - outh2))
        w5 = w5 - a * d5
        w6 = w6 - a * d6
        w1 = w1 - a * d1
        w2 = w2 - a * d2
        w3 = w3 - a * d3
        w4 = w4 - a * d4
        b1 = b1 - a * tb1
        b2 = b2 - a * tb2
        print('w1: %.2f w2: %.2f w3: %.2f w4: %.2f w5: %.2f w6: %.2f' % (w1, w2, w3, w4, w5, w6))
        print('b1: %.2f b2: %.2f' % (b1, b2))

BP()