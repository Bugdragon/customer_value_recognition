#  数据标准差标准化

import pandas as pd

data = pd.read_excel('./data/zscoredata.xls')
result = './result/zscoreddata.xls'

data = (data - data.mean(axis=0)) / (data.std(axis=0))  # 标准差标准化
data.columns = ['Z' + i for i in data.columns]

data.to_excel(result, index=False)
