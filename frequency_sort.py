def frequency_sort(c):
    a = []
    a += c
    b = [] 
    g = 0
    count = []
    count_result = []
    while True:
        if not a:
            break
        b.append(a[0])
        for i in range(0, a.count(a[0])):
            a.pop(a.index(b[g]))
        g += 1
    if b == c:
        return c
    for i in range(0, len(b)):
        count.append(c.count(b[i]))
    count_save = []
    count_save += count
    for i in range(0, len(count)):
        count_result.append(max(count))
        count.pop(count.index(max(count)))
    result_list = []
    result_b = [None] * len(b)
    indexNum = []
    for i in range(0, len(b)):
        indexNum.append(count_result.index(count_save[i]))
        if result_b[indexNum[i]] != None:
            indexNum[i] += 1
        result_b[indexNum[i]] = b[i]
    for i in range(0, len(result_b)):
        result_list = result_list + [result_b[i]] * count_result[i]
    return result_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]