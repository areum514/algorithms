def binary_search(list, target):
    low = 0
    high = len(list)-1

    while low <= high:
        middle = low+high//2
        guess = list[middle]

        if guess > target:
            high = middle - 1
        elif guess < target:
            low = middle + 1
        else:
            return middle
    return None


print(binary_search([1, 3, 2], 3))

# 정렬된 리스트에서
# 가운데 값을 부른다
# 가운데 값이 찾고자 하는 값보다 크면
# end를 가운데로

# 가운데 값이 찾고자 하는 값보다 작으면
# start를 가운데로
