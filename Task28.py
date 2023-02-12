# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# 2 2
# 4

def new_sum(a,b):
    if a > 0:
        return 1 + new_sum(a-1,b)
    elif b > 0:
        return 1 + new_sum(a, b-1)
    return 0

print(new_sum(int(input('Input number A: ')), int(input('Input number B: '))))