import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandowWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=5)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # plt.savefig('squares_plot.png', bbox_inches='tight')
    plt.show()

    keep_running = input()
    if keep_running == 'n':
        break