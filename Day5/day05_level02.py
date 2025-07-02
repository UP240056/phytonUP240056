# Original List
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(ages)

min_age = min(ages)
print("Número más pequeño: ",min_age)

max_age = max(ages)
print("Número más grande: ",max_age)

median_age = ages[4:5]
average_age = sum(ages) / len(ages)
range_ages = min_age, max_age

dif_min_avg = abs(min_age - average_age)
dif_max_avg = abs(max_age - average_age)

