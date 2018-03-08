#  数据预分析：统计每个属性的缺失值个数，查找最大、最小值。

import pandas as pd

data = pd.read_csv('./data/air_data.csv', encoding='utf-8')  # 导入航空客户原始数据,指定UTF-8编码
result = './result/explore.xls'  # 导出缺失值个数，最大值，最小值

explore = data.describe().T  # percentiles指定计算多少的分位数表，计算非空值数
#  describe函数包括count，mean，std，min，25%，50%，75%，max

explore['null'] = len(data) - explore['count']  # 计算空值数
explore = explore[['null', 'max', 'min']]  # 取空值数，最大值，最小值
explore.columns = [u'缺失值个数', u'最大值', u'最小值']  # 表头重命名

explore.to_excel(result)
