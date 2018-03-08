#  数据清洗：丢弃满足清洗条件的数据

import pandas as pd

data = pd.read_csv('./data/air_data.csv', encoding = 'utf-8')
result = './result/data_cleaned.csv'  # 导出数清洗后的数据

data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]  # 保留总票价非空值

term_1 = data['SUM_YR_1'] != 0
term_2 = data['SUM_YR_2'] != 0
term_3 = data['avg_discount'] == 0
data = data[term_1 | term_2 | term_3]  # 保留票价非零值或平均折扣率为零的值

data.to_csv(result, sep=",", encoding='utf-8')