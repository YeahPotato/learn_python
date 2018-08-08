from _collections_abc import Iterable

# 迭代
t = (1,2,3)
l = [1,2,3]
d = {'name':1,'age':3}
s = set(d)

# for n in t:
#     print(n)
#
# for m in l:
#     print(m)
#
# for k,v in d.items():
#     print(k,v)
#
# for x in s:
#     print(x)

# 判断一个对象是否是可迭代对象
print(isinstance(l,Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,val in enumerate(l):
    print(i,val)

### p 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L==[]:
        return (None,None)
    else:
        min = L[0]
        max = L[0]
        for d in L:
            if d<min:
                min = d
            elif d>max:
                max = d

        return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

