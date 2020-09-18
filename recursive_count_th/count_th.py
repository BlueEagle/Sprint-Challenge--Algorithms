'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    keyword = "th"
    location = word.find(keyword)
    if word:
        if location == -1:
            return 0
        else:
            return 1 + count_th(word[location+len(keyword):])
    else:
        return 0
