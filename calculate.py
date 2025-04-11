# calculate.py - 改进版本

def fib(n: int):
    """
    生成长度为 n 的斐波那契数列。

    参数:
        n (int): 数列的长度, 必须为正整数

    返回:
        list: 包含 n 个斐波那契数, 如果 n <= 0, 返回空列表

    异常:
        ValueError: 当 n 不是正整数时抛出异常
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("参数 n 必须是非负整数")
    if n == 0:
        return []
    elif n == 1:
        return [0]
    result = [0, 1]
    while len(result) < n:
        # 通过相邻两个数之和生成下一个斐波那契数
        next_value = result[-1] + result[-2]
        result.append(next_value)
    return result

if __name__ == '__main__':
    try:
        length = int(input("请输入斐波那契数列的长度: "))
        print("Fibonacci sequence:", fib(length))
    except ValueError as e:
        print("输入错误:", e)

