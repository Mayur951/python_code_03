def get_value(obj, key):
# This will make the list
    keys = key.split('/')
    #print (keys)
    val = obj
    for k in keys:
        val = val[k]
        #print (val)
    return val


print (get_value({"a":{"b":{"c":"d"}}}, "a/b/c" ))
