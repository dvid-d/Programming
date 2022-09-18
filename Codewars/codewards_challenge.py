# https://www.codewars.com/kata/5533c2a50c4fea6832000101
keys = ['a','b','c']
values = [1, 2, 3, 4]

def createDict(keys, values):
    while len(keys) > len(values):
        values.append(None)
    dictionary = dict(zip(keys, values))
    print(dictionary)

if __name__ == '__main__':
    createDict(keys,values)
