import datetime
print(datetime.datetime.today())
import matplotlib.pyplot as plt

data_x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
data_y = [30, 25, 95, 115, 265, 325, 570, 700, 1085, 1300]

def calculate_mean(values):
    return sum(values) / len(values)

def calculate_variance(values, mean_val):
    return sum([(val - mean_val)**2 for val in values])

def calculate_covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

average_x, average_y = calculate_mean(data_x), calculate_mean(data_y)

beta1 = calculate_covariance(data_x, average_x, data_y, average_y) / calculate_variance(data_x, average_x)
beta0 = average_y - beta1 * average_x

print('Coefficients: b1=%.3f, b0=%.3f' % (beta1, beta0))

numerator = sum([(data_x[i] - average_x) * (data_y[i] - average_y) for i in range(len(data_x))])
denominator = (sum([(x_val - average_x) ** 2 for x_val in data_x]) * sum([(y_val - average_y) ** 2 for y_val in data_y])) ** 0.5
correlation_r = numerator / denominator

print('Correlation coefficient: r=%.3f' % correlation_r)

line = [beta0 + beta1 * x_val for x_val in data_x]

plt.scatter(data_x, data_y, color='blue', label='Actual points')
plt.plot(data_x, line, color='red', label='Regression line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.show()
