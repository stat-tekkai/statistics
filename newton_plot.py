import numpy as np
import matplotlib.pyplot as plt
from statistics import mean, median,variance,stdev

from scipy.stats import chi2


N=500 #プロットする点の数
x = np.random.uniform(0.0, 1.0, N)
y = np.random.uniform(0.0, 1.0, N)

parts = 10 #分割の数
theo = N/parts/parts #理論値

sample = np.full((parts, parts), theo)

#y成分で点をふるいわける
def y_split(i, j, k):
    if k == 0:
        if y[i] <=1/parts:
            sample[j, k] -= 1
    else:
        if  y[i] > k/parts and y[i] <= (k+1)/parts:
            sample[j, k] -= 1



for i in range(N):
    for j in range(parts):
        if j == 0:
            if x[i] <=1/parts:
                for k in range(parts):
                    y_split(i, j, k)
        else:
            if x[i] > j/parts and x[i] <= (j+1)/parts:
                for k in range(parts):
                    y_split(i, j, k)

#それぞれの成分を2乗
for i in range(parts):
    for j in range(parts):
        sample[i, j] *=sample[i, j]

chi = sum(sum(sample))/theo #カイ二乗値を計算
print(chi)
plt.scatter(x, y)

# 自由度100のカイ二乗分布のグラフ
# xx = np.linspace(0, 200 ,100000)
# plt.plot(xx, chi2.pdf(xx, df=100), linewidth=2, color="r")

plt.show()
