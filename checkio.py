def checkio(data: list) -> list:
    a = data
    b = [None] * len(a)
    for i in range(0,len(a)):
        for g in range(i+1,len(a)):
            if a[i] == a[g]:
                b[i] = a[i]
                b[g] = a[g]
    while None in b:
        index_b = b.index(None)
        b.pop(index_b)
    return b


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
