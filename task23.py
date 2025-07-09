def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = dict()
    for i, num in enumerate(numbers):
        group.setdefault(num, []).append(i)
    return group

nums = [3, 6, 7, 9, 3, 1, 4, 6, 1, 6, 9, 71]
result = group_indices(nums)
print(result)