import math
from typing import List, Tuple
Coords = List[Tuple[int, int]]


def find_lenght(coor: list):
    ab = math.sqrt((coor[1][0] - coor[0][0])**2 + (coor[1][1] - coor[0][1])**2)
    bc = math.sqrt((coor[2][0] - coor[1][0])**2 + (coor[2][1] - coor[1][1])**2)
    ac = math.sqrt((coor[2][0] - coor[0][0])**2 + (coor[2][1] - coor[0][1])**2)
    return [ab, bc, ac]

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    a = find_lenght(coords_1)
    b = find_lenght(coords_2)
    a = sorted(a)
    b = sorted(b)
    return a[0]/b[0]/10==a[1]/b[1]/10==a[2]/b[2]/10


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([[2,1],[3,4],[-3,1]],[[-10,-3],[8,6],[5,-3]]))
        # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")