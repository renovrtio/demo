import pygal
from die import Die

# 创建一个Die

def get_frequencies():
    # 创建一个Die
    die = Die()

    # 掷几次骰子，并将结果存储在一个列表中
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    return frequencies

frequencies1 = get_frequencies()
frequencies2 = get_frequencies()

# 对解脱进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.y_labels = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
hist.y_title = 'Frequency of Result'

hist.add('D61', frequencies1)
hist.add('D62', frequencies2)
hist.render_to_file('die_visual.svg')

print(frequencies1)
