def words_order(text: str, words: list) -> bool:
    indexOrder = []
    text = text.split(' ')
    for i in range(0, len(words)):
        try:
            indexOrder.append(text.index(words[i]))
        except ValueError:
            return False
    for i in range(0, len(indexOrder)):
        for g in range(i+1, len(indexOrder)):
            if indexOrder[i] == indexOrder[g]:
                return False
    indexOrderSorted = sorted(indexOrder)
    if indexOrder == indexOrderSorted:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))