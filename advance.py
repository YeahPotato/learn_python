# 高级特性
## 切片 slice
l = ['joke','june','nine','ketty']
b = l[:3]  #0-3
b = l[1:4] #1-4
b = l[-2:] # 倒数第二个到完
b = l[-2:-1] #倒数第二个到倒数第一个
a = list(range(10,100));
b = a[::10]
print(b)

### P 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(str):
    if len(str)==0:
        return ''
    else:
        if str[0]==' ':
            return trim(str[1:])
        elif str[-1]==' ':
            return trim(str[:-1])
        else:
            return str


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
