def second_index(text: str, symbol: str) -> [int, None]:
    text = list(text)
    try:
        textIndex = text.index(symbol)
        text.pop(textIndex)
        result = text.index(symbol)
    except ValueError:
        return None
    return result


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", " "))