def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}
    for key in d:
        value = d[key]
        if value != 0:
            result[key] = value
    return result

data = {
    'a': 1,
    'b': 2,
    'c': 4,
    'd': 0,
    'e': -2,
    'f': 0
}

result = filter_non_zero(data)
print(result)