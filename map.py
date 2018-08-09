# map
from functools import reduce


def f(x):
    if(x>10):
        return x

g =list(map(f,list(range(100))));
print(g)



l = [1,3,5,7,9]
def r(res,n):
    return str(res)+str(n)
print(reduce(r,l))


### p 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    if isinstance(name,str):
        return name[0].upper()+name[1:].lower()
    else:
        pass

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



###p回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    temp = str(n)
    return temp == temp[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
