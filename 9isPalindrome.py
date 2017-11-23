def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    # str1=str(x)
    # len_s=len(str1)
    # n=0
    # while n<=len_s//2 and str1[n]==str1[-(n+1)]  :n=n+1
    # if n>len_s//2 :return True
    # else:return False
    return str(x) == str(x)[::-1]