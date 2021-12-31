import numpy as np
operations_at_once = 100
times_opened = [24.012, 27.710, 19.197]
times_closed = [22.297, 16.491, 23.447]

sum_time_opened = 0
sum_time_closed = 0
sum_operations = 0
for i in times_opened:
    sum_time_opened += i
    sum_operations += operations_at_once


for i in times_closed:
    sum_time_closed += i

open_mean = sum_operations / sum_time_opened
closed_mean = sum_operations / sum_time_closed

standard_deviation_opened = np.std(times_opened, ddof=1)
standard_deviation_closed = np.std(times_closed, ddof=1)

print(f'Total mean opening time: {open_mean}')
print(f'Total mean closing time: {closed_mean}')
print(f'Standard deviadion for opening time: {standard_deviation_opened}')
print(f'Standard deviadion for closing time: {standard_deviation_closed}')
