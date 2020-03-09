def merge(arr1, arr2):
    # merge sorted arrays into a single one
    return 0

if __name__ == '__main__':
    arr1 = [-4, -2, 1, 8]
    arr2 = [1, 4, 6, 10, 14]
    exp = [-4, -2, 1, 1, 4, 6, 8, 10, 14]

    try:
        assert(exp == merge(arr1, arr2))
        print("Implemented Correctly")
    except AssertionError:
        print("Incorrect Implementation")
        
