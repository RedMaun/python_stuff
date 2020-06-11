def split_list(items: list) -> list:
    parity = len(items)%2
    splitPoint = 0
    if parity == 1:
        splitPoint = int(len(items)/2+0.5)
    if parity == 0:
        splitPoint = len(items)//2
    firstList = []
    secondList = []
    for i in range(0, splitPoint):
        firstList.append(items[i])
    for i in range(splitPoint, len(items)):
        secondList.append(items[i])
    return [firstList, secondList]

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5]))