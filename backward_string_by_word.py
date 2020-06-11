# -*- coding: utf-8 -*-
def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

def backward_string_by_word(text: str) -> str:
    if not text:
        return text
    list_text = list(text)
    word = []
    result = []
    final = []
    for i in range(0, len(list_text)):
        if list_text[i] != " ":
            word.append(list_text[i])
        if list_text[i] == " " or i+1 == len(list_text):
            result = [None] * len(word)
            for g in range(0, len(word)):
               result[g] = word[len(word)-1-g]
            word.clear()
            final += result
            result.clear()
            final.append(list_text[i])
    final.pop()
    final = listToString(final)
    return final

print(backward_string_by_word('bla alb bla bla'))