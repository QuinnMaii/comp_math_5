import numpy as np
from math import pi
import functions

def create_basic_polynomial(points, i):
    def basic_polynomial(x):
        upper_part = 1
        divider_part = 1
        for j in range(len(points)):
            if j != i:
                upper_part *= (x - points[j][0])
                divider_part *= (points[i][0] - points[j][0])
        return upper_part / divider_part

    return basic_polynomial


def create_Lagrange_polynomial(points):
    basic_polynomials = []
    for i in range(len(points)):
        basic_polynomials.append(create_basic_polynomial(points, i))

    def lagrange_polynomial(x):
        result = 0
        for j in range(len(points)):
            result += points[j][1] * basic_polynomials[j](x)
        return result

    return lagrange_polynomial


def euler_method(initial_point, function_id, h, n):
    x_current = initial_point[0]
    y_current = initial_point[1]
    points = [[x_current, y_current]]
    for i in range(n):
        x_current+= h
        y_current += h * functions.get_function(function_id, x_current + h/2, y_current + h/2 * functions.get_function(function_id, x_current, y_current))
        points.append([x_current, y_current])
    return points

