import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24

np.random.seed(12)

# x轴的采样点
x = np.linspace(0, 5, 1000000)

# 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……
y = 2*np.sin(x) + 0.3*x**2
y_data = y + np.random.normal(scale=0.3, size=1000000)

# figure()指定图表名称
plt.figure('data')

# '.'标明画散点图，每个散点的形状是个圆
plt.plot(x, y_data, '.')
# 将当前figure的图保存到文件result.png
plt.savefig('result.png')

# 一定要加上这句才能让画好的图显示在屏幕上
plt.show()