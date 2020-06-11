from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 1 or len(elements) == 0:
        return True
    for i in range(1, len(elements)):
        if elements[0] != elements[i]:
            return False
    return True 

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1,2,3,4,5,6]))