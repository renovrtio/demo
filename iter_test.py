import sys

def fibonacci(n):
    '''生成器函数 - 斐波那契'''
    a, b ,counter = 0, 1, 0
    while True:
        if (counter > n):
            break
        yield a
        a, b = b, a + b
        counter += 1

# f 是一个迭代器，由生成器返回生成
f = fibonacci(10)

while True:
    try:
        value = next(f)
        print(value)
    except StopIteration as identifier:
        sys.exit()


list=[1, 2, 3, 4]
it = iter(list)

print(type(it))

for var in it:
    print(var)