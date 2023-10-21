
import datetime
print(datetime.datetime.today())

import random

def mean(lst):
    return sum(lst) / len(lst)

def standard_deviation(lst, mu):
    return (sum([(x - mu) ** 2 for x in lst]) / len(lst)) ** 0.5

def verify_Chebyshev_ineq(lst, k):
    mu = mean(lst)
    sd = standard_deviation(lst, mu)
    
    count = sum([1 for x in lst if mu - k*sd <= x <= mu + k*sd])
    probability = count / len(lst)
    chebyshev_bound = 1 - 1 / (k**2)
    
    print(f"Probability of |X-u| = {probability:.2f} ; 1-1/(k^2)= {chebyshev_bound}")
    if probability >= chebyshev_bound:
        print(f"When k = {k} , P(|X-u|<k*sd)>=1-1/k^2 is True")
    else:
        print(f"When k = {k} , P(|X-u|<k*sd)>=1-1/k^2 is False")
    return count


lst = [random.gauss(10, 0.5) for _ in range(50)]


for k in [1, 2**0.5, 1.5, 2, 3]:
    cnt = verify_Chebyshev_ineq(lst, k)

print("\n----- Uniform Distribution Verification -----\n")

# For Uniform Distribution
lst = [random.uniform(-20, 20) for _ in range(50)]

# Testcases for uniform distribution
for k in [1, 2**0.5, 1.5, 2, 3]:
    cnt = verify_Chebyshev_ineq(lst, k)
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

X = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
Y = np.array([30, 25, 95, 115, 265, 325, 570, 700, 1085, 1300])


slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

print(f'b1 (Slope) = {slope}')
print(f'b0 (Intercept) = {intercept}')
print(f'Coefficient of Linear Correlation (r) = {r_value}')


line = slope * X + intercept


plt.scatter(X, Y, color='blue', label='Data points')
plt.plot(X, line, color='red', label=f'Fitted line: Y = {slope:.2f}*X + {intercept:.2f}')
plt.title('Linear Regression on X vs Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Evaluating the model
if 0.7 < r_value < 1:
    print("The linear model seems to be a good fit for this dataset as the value of r is very close to +1.")
else:
    print("The linear model may not be the best fit for this dataset as the value of r is not very close to +1.")

# Suggestion for a better fitting model based on data visualization
print("\nimport random")

def calc_mean(values):
    return sum(values) / len(values)

def calc_std_dev(values, average):
    return (sum([(x - average) ** 2 for x in values]) / len(values)) ** 0.5

def check_chebyshev(values, factor):
    avg = calc_mean(values)
    std_dev = calc_std_dev(values, avg)
    
    within_range = sum([1 for x in values if avg - factor * std_dev <= x <= avg + factor * std_dev])
    prob = within_range / len(values)
    chebyshev_lim = 1 - 1 / (factor**2)
    
    print(f"Probability of |X-u| = {prob:.2f} ; 1-1/(k^2)= {chebyshev_lim}")
    print(f"When k = {factor} , P(|X-u|<k*sd)>=1-1/k^2 is {'True' if prob >= chebyshev_lim else 'False'}")
    return within_range

normal_dist_data = [random.gauss(10, 0.5) for _ in range(50)]

for factor in [1, 2**0.5, 1.5, 2, 3]:
    check_chebyshev(normal_dist_data, factor)

print("\n----- Uniform Distribution Verification -----\n")

uniform_dist_data = [random.uniform(-20, 20) for _ in range(50)]

for factor in [1, 2**0.5, 1.5, 2, 3]:
    check_chebyshev(uniform_dist_data, factor)
