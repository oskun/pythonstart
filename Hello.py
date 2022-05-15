brands = ['mac', 'IBM', "TCL", 'lenovo', 'acer', 'amd']
indexs = []
len = len(brands) - 1
for index in range(len):
    if ("mac" in brands[index] or "amd" in brands[index]):
        indexs.append(index)
# 这里犯错误，index 已经改变
for index in indexs:
    del brands[index]


# 判断在列表中
# test git
# 判断表达式
print(brands)
