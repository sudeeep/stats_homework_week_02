import datetime
print(datetime.datetime.today())

import pandas as pd
import matplotlib.pyplot as plt

def mean(values):
    return sum(values) / len(values)

def variance(values, sample=False):
    mean_val = mean(values)
    return sum((x - mean_val) ** 2 for x in values) / (len(values) - int(sample))

def standard_deviation(values, sample=False):
    return variance(values, sample) ** 0.5

def z_scores(values):
    mean_val = mean(values)
    std_dev = standard_deviation(values)
    return [(x - mean_val) / std_dev for x in values]

def quartiles(values):
    sorted_vals = sorted(values)
    mid = len(sorted_vals) // 2
    if len(sorted_vals) % 2 == 0:
        q1 = median(sorted_vals[:mid])
        q3 = median(sorted_vals[mid:])
    else:
        q1 = median(sorted_vals[:mid])
        q3 = median(sorted_vals[mid+1:])
    return q1, q3

def median(values):
    sorted_vals = sorted(values)
    mid = len(sorted_vals) // 2
    if len(sorted_vals) % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    else:
        return sorted_vals[mid]


df = pd.read_excel('original_diabetes.xlsx')


glucose = df['Glucose'].dropna().tolist()
blood_pressure = df['BloodPressure'].dropna().tolist()

stats = {}
for label, data in zip(["Glucose", "BloodPressure"], [glucose, blood_pressure]):
    stats[label] = {
        "Mean": mean(data),
        "Variance": variance(data),
        "Standard Deviation": standard_deviation(data),
        "Z-scores": z_scores(data),
        "Q1": quartiles(data)[0],
        "Median": median(data),
        "Q3": quartiles(data)[1]
    }
    print(f"{label} Stats: {stats[label]}")


plt.boxplot([glucose, blood_pressure], labels=['Glucose', 'BloodPressure'])
plt.title('Boxplot of Glucose and Blood Pressure')
plt.show()
