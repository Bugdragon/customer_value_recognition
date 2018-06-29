#  属性构造：构造 L R F M C 指标

import pandas as pd

data = pd.read_csv('./result/data_selected.csv', encoding='utf-8')  # 导入属性规约后的数据
result = './result/data_changed.csv'  # 导出属性构造后的数据


def diffMonth(startDate, endDate):
    start = datetime.strptime(startDate, "%y/%m/%d").date()
    end = datetime.strptime(endDate, "%y/%m/%d").date()

    startYear = start.year
    startMonth = start.month
    endYear = end.year
    endMonth = end.month

    # 如果起始日期大于结束日期，报错
    if endYear - startYear < 0 or (endYear - startYear == 0 and endMonth - startMonth < 0):
        print('结束日期必须大于起始日期')
    # 如果不是同年
    else:
        years = endYear - startYear
        diffmonths = years * 12 + endMonth - startMonth
    return int(diffmonths + 1)


for dt in data:
    data[dt]['LOAD_TIME'] = diffMonth(data[dt]['FFP_DATE'], data[dt]['LOAD_TIME'])

data = data[data['LOAD_TIME'], data['LAST_TO_END'] / 31.0, 'FLIGHT_COUNT', 'SEG_KM_SUM', 'AVG_DISCOUNT']
data.columns = [u'L', u'R', u'F', u'M', u'C']  # 按规则构造新属性

data.to_csv(result, sep=",", encoding='utf-8')
