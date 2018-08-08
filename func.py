# abs funciton
# print(abs(-100));

# 数据类型转换
# int float str bool

# 用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

# n1 = 255;
# n2 = 1000;
# print(hex(n1));
# print(hex(n2));

# 函数默认参数
# def pow(m,n=2):
#     x = 1
#     while(n>0):
#         n = n-1
#         x  = x*m;
#         print(x)
#     return x;
#
# print(pow(2,3))

# def add_end(l=[]):
#     l.append('joke')
#     return l

# def add_end(l=None):
#     if l is None:
#         l = []
#     l.append('joke')
#     return l
#
# print(add_end());
# print(add_end());

### 可变参数
# def calc(*numbers):
#     sum = 0
#     for num in numbers:
#         sum = sum+num
#     return sum
#
# t = (1,2,3)
# print(calc(*t))
# print(calc(1,2,3,5))

### 关键字参数
# def person(name,age,**kw):
#     if 'job' in kw:
#         print('has job key')
#     else:
#         pass
#     if 'sex' in kw:
#         print('has sex key')
#     else:
#         pass
#     print(name,age,kw)

# person('joke',18)
# person('joke',18,job='it')

### 类似javascript的数组展开...
# di = {'job':'IT'}
#
# person('joke',18,**di)


#P 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(*args):
#     sum = 1
#     for d in args:
#         sum*=d
#
#     return sum
#
# print(product(4,5,6))

### 递归
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
#
# print(fact(1000))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c);
    else:
         move(n-1, a, c, b)
         move(1, a, b, c)
         move(n-1, b, a, c)

move(4,'a','b','c')

