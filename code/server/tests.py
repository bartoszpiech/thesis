opened_at_once = 100
times_opened = [24.012, 27.710, 19.197]
times_closed = [22.297, 16.491, 23.447]

sum_opened = 0
sum_time_closed = 0
sum_time = 0
for i in times_opened:
    sum_time += i
    sum_opened += opened_at_once


for i in times_closed:
    sum_time_closed += i

open_mean = sum_opened / sum_time
closed_mean = sum_opened / sum_time_closed
#open_mean = sum_time / sum_opened 
#closed_mean = sum_time_closed / sum_opened
print(f'Total mean opening time: {open_mean}')
print(f'Total mean closing time: {closed_mean}')
