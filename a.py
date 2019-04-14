print('输入3个数： \n')
a = int(input())
b = int(input())
c = int(input())
def f(a, b):
    if a > b:
        return a
    return b
def max(a, b, c):
    return f(a, f(b, c))

print('最大数为：', max(a, b, c))
