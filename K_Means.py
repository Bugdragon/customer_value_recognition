#  K-Means聚类算法

import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_excel('./result/zscoreddata.xls')  # 数据读取
k = 5  # 聚类类别数目

# 调用k-means算法
model = KMeans(n_clusters=k, n_jobs=1)  # 输入聚类类别数目，n_jobs为并行数
model.fit(data)  # 训练

#  model.cluster_centers_ 聚类中心
#  labels = model.labels_ 每个样本对应的簇类别标签
r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类中心
r = pd.concat([r2, r1], axis=1)   # 得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别数目']  # 重命名表头
r.to_excel('./result/KMeansNum.xls')

r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)   # 详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别']  # 重命名表头
r.to_excel('./result/KMeans.xls')
