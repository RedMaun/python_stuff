def checkio(number: int) -> int:
    num = list(str(number))
    result = 1
    for i in range(0, len(num)):
        try:
            num.pop(num.index('0'))
        except ValueError:
            break
    for i in range(0, len(num)):
        result *= int(num[i])
    return result
    


if __name__ == '__main__':
    print('Example:')
    print(checkio(1234567))