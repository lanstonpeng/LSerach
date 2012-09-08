def hash_string(keyword,buckets):
    h = 0
    for c in keyword:
        h = (h + ord(c))  % buckets
    return h

def hash_string2(keyword,buckets):
    h = 0
    for c in keyword:
        h+=ord(c)
    return h % buckets
print hash_string2('udacity',12)
