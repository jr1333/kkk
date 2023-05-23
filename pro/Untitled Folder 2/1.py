# 1
import numpy as np

np.random.seed(42)  # 设置随机数种子，以确保结果可复现
mean = 5
variance = 3
random_numbers = np.random.normal(mean, np.sqrt(variance), 2000)
# 2
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.hist(random_numbers, bins='auto', density=True, histtype='stepfilled', alpha=0.7)
plt.xlabel('随机数')
plt.ylabel('频率')
plt.title('服从正态分布的随机数直方图')
plt.show()
# 3
estimated_mean = np.mean(random_numbers)
estimated_variance = np.var(random_numbers)
print("估计的均值:", estimated_mean)
print("估计的方差:", estimated_variance)
