import numpy as np
import random

x = np.array([[1, 1], [2, 2], [2, 0], [0, 0], [1, 0], [0, 1]], float)
y = np.array([[1], [1], [1], [-1], [-1], [-1]], float)
a = np.array([0, 0, 0, 0, 0, 0], float)


def J(i, ei):
    max = 0
    maxj = 0
    for j in range(6):
        ej = g(j)-y[j]
        if abs(ei-ej) > max and i != j :
            max = abs(ei-ej)
            maxj = j
    return maxj


def K(i, j):
    return np.dot(x[i], x[j])


def g(x):
    gx = 0
    for i in range(6):
        gx += a[i]*y[i]*K(x, i)
    return gx


def svm():
    C = 1
    b = cnt = 0
    while cnt < 100:
        cnt += 1
        for i in range(6):
            gxi = g(i) + b
            Ei = gxi - y[i]
            if (y[i]*Ei < -0.5 and a[i] < C) or (y[i]*Ei > 0.5 and a[i] > 0):
                j = J(i, Ei)
                gxj = g(j) + b
                Ej = gxj - y[j]
                aiold = a[i].copy()
                ajold = a[j].copy()
                if y[i] != y[j]:
                    L = max(0, a[j]-a[i])
                    H = min(C, C+a[j]-a[i])
                else:
                    L = max(0, a[j]+a[i] - C)
                    H = min(C, a[j]+a[i])
                a[j] = a[j] + y[j]*(Ei-Ej)/(K(1, 1)+K(2, 2)-2*K(1, 2))
                a[j] = H if a[j] >= H else a[j]
                a[j] = L if a[j] <= L else a[j]
                a[j] += y[j] * y[i] * (ajold - a[j])
                b1 = b - Ei - y[i] * (a[i] - aiold) * K(i, i) - y[j] * (a[j] - ajold) * K(i, j)
                b2 = b - Ej - y[i] * (a[i] - aiold) * K(i, j) - y[j] * (a[j] - ajold) * K(j, j)
                if 0 < a[i] < C:
                    b = b1
                elif 0 < a[j] < C:
                    b = b2
                else:
                    b = (b1+b2)/2.0
            cnt += 1
    return b


p = svm()
w = 0
for i in range(6):
    w += a[i]*y[i]*x[i]
print(w)
print(p)
