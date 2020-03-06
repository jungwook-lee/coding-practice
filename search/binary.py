def binary_search(num, val):
    l, r = 0, len(num)
    while l < r:
        mid = l + (r - l) // 2
        if num[mid] == val:
            return mid
        elif num[mid] < val:
            l = mid + 1
        else:
            r = mid - 1
    return -1


if __name__ == '__main__':
    test = [1,2,3,4,5,6,7,8]
    print(binary_search(test, 7))
