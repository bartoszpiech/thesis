import numpy as np
data = [(25923, 7.312), (25904, 7.115), (25897, 7.046), (25908, 7.208), (25937, 7.276)]
l = []

for d in data:
    l.append(d[1])

print(l)
sum_bytes = 0
sum_time = 0
for d in data:
    sum_bytes += d[0]
    sum_time += d[1]

mean = sum_bytes / sum_time
standard_deviation = np.std(l, ddof=1)
print(f'Total mean time: {mean}')
print(f'Standard deviation: {standard_deviation}')
