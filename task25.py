from typing import Union

def group_by_age(people: list[dict[str, Union[int, str]]]) -> dict[int, list[str]]:
    group = {}
    for person in people:
        if isinstance(person['age'], int):  
            group.setdefault(person['age'], []).append(person['name'])
    return group

people = [
    {"age": 13, "name": "Vali"},
    {"age": 15, "name": "Ali"},
    {"age": 10, "name": "Sami"},
    {"age": 12, "name": "Jon"},  
]

result = group_by_age(people)
print(result)
