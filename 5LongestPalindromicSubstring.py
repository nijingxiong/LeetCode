def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    len_s = len(s)
    len_max = 0
    i, j, n, t = 0, 0, 1, 0
    max_n = 0
    if len_s == 1: return s
    while i < len_s:
        while i + n < len_s and s[i] == s[i + n]:
            n = n + 1
        n = n - 1
        while i - j >= 0 and i + j + n < len_s and s[i - j] == s[i + n + j]:
            j = j + 1
        if (j - 1) * 2 + n + 1 >= len_max:
            len_max = (j - 1) * 2 + n + 1
            t = i
            max_n = n
        j = 0
        n = 1
    if len_max == 0: return s[0]
    return s[t - (len_max - 1 - max_n) // 2:t + max_n + (len_max - 1 - max_n) // 2 + 1]