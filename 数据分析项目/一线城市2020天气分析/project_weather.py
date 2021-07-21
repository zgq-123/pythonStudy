import pandas as pd

# 读取文件并合并
# city_list = '北京,上海,广州,深圳'.split(',')
# path_list = [f'数据/{i}历史天气.xlsx' for i in city_list]
# df_list = []
# for path in path_list:
#     df = pd.read_excel(path)
#     df['地区'] = path[2:4]
#     df_list.append(df)  # 新增一列地区
# df_p = pd.concat(df_list)  # 合并四个表格的数据
# columns = df_p.columns.to_list
# data = df_p.values
# print(data)
# m = pd.DataFrame(columns=columns, data=data)
# m.to_excel('test.xlsx', encoding='gbk')

data = {
    [2000, 2001, 2002, 2001, 2002],
    [1, 2, 3, 4, 5]
}
print(type(data))
