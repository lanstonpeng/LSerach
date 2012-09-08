def is_palindorme(word):
    if len(word)  <= 1 :
        return True
    if word[0] == word[-1]:
        return is_palindorme(word[1:-1])
    return False

print is_palindorme('level')
