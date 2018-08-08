# 列表生成式
import os


l = [d for d in os.listdir('.')]
a = [m+n for m in 'ABC' for n in 'abc']
print(a)

### p L1 = ['Hello', 'World', 18, 'Apple', None]
L1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [n.lower() for n in L1 if isinstance(n,str)]
print(l2)