n = int(input())
input_list = list(map(int, input().split()))

temp_list = []
start_i = -1
end_i = -1
for i in range(n):
    if input_list[i] == max(input_list) or input_list[i] == min(input_list):
        if start_i == -1:
            start_i = i
        else:
            end_i = i

import math

print(f'{sum(i for i in input_list if i > 0)} {math.prod(input_list[start_i+1:end_i])}')