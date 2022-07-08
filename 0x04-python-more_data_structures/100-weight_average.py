#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        div = 0
        mul_sum = 0
        for i in my_list:
            mul = i[0] * i[1]
            mul_sum = mul_sum + mul
            div = div + i[1]
            result = mul_sum / div
        return result
    else:
        return 0
