def reverse(s):
    s = list(s)
    for i in range(0, len(s) // 2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
    return "".join(s)
        

def reverse_substring(s, l, r):
    s = list(s)
    word_len = r - l
    for i in range(0, word_len // 2):
       s[l + i], s[r - i] = s[r - i], s[l + i]
    return "".join(s)

if __name__ == '__main__':
    test = "abcde fghij"
    print(reverse(test))
    print(reverse_substring(test, 6, 10))

