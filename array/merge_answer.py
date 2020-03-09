def merge(arr1, arr2):
    # merges sorted arrays into a single one
    out = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            out.append(arr1[i])
            i += 1
        elif arr1[i] >= arr2[j]:
            out.append(arr2[j])
            j += 1
    while i < len(arr1):
        out.append(arr1[i])
        i+=1
    while j < len(arr2):
        out.append(arr2[j])
        j+=1
    return out


if __name__ == '__main__':
    arr1 = [-4, -2, 1, 8]
    arr2 = [1, 4, 6, 10, 14]
    print(merge(arr1, arr2))
