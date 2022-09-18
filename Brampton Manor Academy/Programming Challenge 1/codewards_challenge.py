keys = ['a','b','c']
values = [1, 2, 3, 4]

def createDict(keys, values):
    while len(keys) > len(values):
        values.append(None)
    dictionary = dict(zip(keys, values))
    print(dictionary)

if __name__ == '__main__':
    createDict(keys,values)
