# 生成器   相比列表生成式而言 生成器更加节省空间
# 生成器保存的是算法，不是值

g = (x*x for x in list(range(10)))
print(g)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g',x)
#     except StopIteration as e:
#         print('Generator return value',e)
#         break;


# 杨辉三角
def triangles(times):
    L = [1]
    while times:
        yield L
        if len(L) == 1:
             L=L+[1]
        else:
            times-=1
            L = [L[x]+L[x+1] for x in range(len(L)-1)]
            L.insert(0,1)
            L.append(1)

ge = triangles(10)

for x in ge:
    print(x)
