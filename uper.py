from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 1 or len(elements) == 0:
        return True
    for i in range(1, len(elements)):
        if elements[0] != elements[i]:
            return False
    return True 

def is_all_upper(a):
    a = a.split(" ")
    ans = []
    for i in range(0, len(a)):
        ans.append(a[i].isupper())
    if all_the_same(ans) == True:
        if ans[0] == False:
            return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")