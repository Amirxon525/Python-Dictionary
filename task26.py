def merge_dicts(a: dict, b: dict) -> dict:
 result = dict()
 result. update(a)
 result. update (b)
 return result
a = {'a'
: 2, "b": 7}
b = {'c':
4,
'd': 9}
result = merge_dicts (a, b)
print (result)