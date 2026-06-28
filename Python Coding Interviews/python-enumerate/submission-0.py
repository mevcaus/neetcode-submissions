from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for index, num in enumerate(nums):
        if num == 7:
            return index
    return -1
    pass


def get_dist_between_sevens(nums: List[int]) -> int:
    index_of_seven = []
    for index, num in enumerate(nums):
        if num == 7:
            index_of_seven.append(index)
    return abs(index_of_seven[0] - index_of_seven[1])
    pass


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
