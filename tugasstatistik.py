#Mean
[4, 8, 15, 16, 23, 42]
data_mean = [4, 8, 15, 16, 23, 42]
mean = sum(data_mean) / len(data_mean)

print(f"Mean: {mean}")

#Median
[10, 20, 30, 40, 50]
data_median = [10, 20, 30, 40, 50]
data_median.sort()

if len(data_median) % 2 == 0:
    median = (data_median[len(data_median)//2 - 1] + data_median[len(data_median)//2]) / 2
else:
    median = data_median[len(data_median)//2]

print(f"Median: {median}")

#Modus
[7, 1, 3, 7, 2, 7, 4, 5]
data_modus = [7, 1, 3, 7, 2, 7, 4, 5]
modus = max(set(data_modus), key=data_modus.count)

print(f"Modus: {modus}")