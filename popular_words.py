def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    text = text.split()
    count = []
    dict_of_popular_words = {}
    for i in range(0, len(words)):
        if words[i] in text:
            count.append(text.count(words[i]))
        else:
            count.append(0)
    for i in range(0, len(words)):
        dict_of_popular_words.update( { words[i] : count[i] } )
    return dict_of_popular_words

if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was']))