# 列表的切片操作
list1 = ['热巴', '冬妮娅', '杨幂', 'Java', 'Python', "100", "99"]
print(list1)
newlist = sorted(list1)
print(newlist)
newlist = sorted(list1, reverse=True)
print(list1)
list2 = list1 * 3
print(list2)
print(list(range(1, 10, 3)))

# 枚举
l1 = ['a', 'abc', 'jk', 'opop']
for index, vaule in enumerate(l1):
    print(index, vaule,end='$')
