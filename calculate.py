# calculate.py - 初始版本

def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    result = [0, 1]
    while len(result) < n:
        # 直接将当前两个数相加得到下一个数字
        result.append(result[-1] + result[-2])
    return result

if __name__ == '__main__':
    print("Fibonacci sequence:", fib(10))

