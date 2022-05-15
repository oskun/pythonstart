import random

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
    print(index, vaule, end='$')

# 元组
t1 = ('hello', 12)
print(t1)

list1 = []

for i in range(10):
    ran = random.randint(1, 20)
    list1.append(ran)
t2 = tuple(list1)
print(t2)
print(t2[2:-3])
max(t2)

# 求和
s1 = sum(t2)
print("s=", s1)

t3 = (9,)
a, *b = t3
print(*b)
