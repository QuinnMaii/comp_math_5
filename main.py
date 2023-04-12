import sys

import functions
import math_solve


def hello():
    print("Laboratory No. 5: \" Numerical differentiation and the Cauchy problem\"")
    print("Option: Modified Euler Method")
    print("Mai Thi Le Quyen, P32302\n")
    print_line()


def print_line():
    print("")


def start_ui():
    is_enter_not_good = True
    while is_enter_not_good:
        functions.print_functions()
        functions_id = is_number(input("> "))
        if 1 <= functions_id <= 4:
            is_enter_not_good = False
            n = enter_amount()
            h = enter_step()
            initial_point = enter_initial_point()
            result_points = math_solve.euler_method(initial_point, functions_id, h, n)
            print_line()
            print_result(result_points)
            functions.plot_graph(functions_id, result_points)
        else:
            print("The " + str(int(functions_id)) + " function doesn't exist.")
            print_line()


def enter_amount():
    print_line()
    n = 0
    is_good_enter = True
    print("Enter a value for n (number of points):")
    while is_good_enter:
        n = int(input("> "))
        if n > 0:
            is_good_enter = False
        else:
            print("The number of points must be greater than 0. Please try again.")
    return n


def enter_step():
    print_line()
    print("Enter h value (step):")
    h = -1
    is_good_enter = True
    while is_good_enter:
        h = is_number(input("> "))
        if h <= 0.0:
            print("The step value must be greater than 0. Please try again.")
        else:
            is_good_enter = False
    return h


def enter_initial_point():
    print_line()
    print("Enter the initial x value:")
    x = is_number(input("> "))
    print_line()
    print("Enter initial y value:")
    y = is_number(input("> "))
    initial_point = [x, y]
    return initial_point


def print_result(points):
    print("Calculated Points:")
    for i in points:
        print("x = {:6.5f}".format(i[0]) + "; y = {:6.6f}".format(i[1]))
    return 0


def is_number(s):
    try:
        if float(s) or s.isnumeric():
            return float(s)
        else:
            print("Had to enter a number. The system is overloaded, it's depressed, start it later.")
            sys.exit()
    except ValueError:
        print("Had to enter a number. The system is overloaded, it's depressed, start it later.")
        sys.exit()


hello()
start_ui()