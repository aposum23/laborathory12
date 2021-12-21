def recursion(n):
    if n == 0:
        print(n)
        return
    else:
        print(n)
        recursion(n - 1)


if __name__ == '__main__':
    number = int(input('Введите число: '))
    recursion(number)