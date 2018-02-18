import csv
from matplotlib import pyplot as plt
from datetime import datetime

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'

# 从文件中获取日期和最高气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    next(reader)    
    # print(header_row)

    # print(type(reader))
    # for index, column_header  in enumerate(header_row):
    #     print(index, column_header)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError as err:
            print(current_date, err)
        else:
            dates.append(current_date)
            highs.append(high)            
            lows.append(low)
            
    print(dates)

# 根据数据绘制图表
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title('每日最低高温，2014年', fontsize=24)
plt.xlabel('日期', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('温度（F）', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# print(datetime.strptime('2014-7-1', '%Y-%m-%d'))

plt.show()