def hastable_add(htable,key,value):
    bucket = hashtable_get_bucket(table,key)
    bucket.append([key,value])

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket :
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key,value])
