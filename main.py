# CHECK PALINDROME

def isPalindrome(S, start, end):
    if start >= end:
        return True
    if S[start] != S[end]:
        return False
    return isPalindrome(S, start + 1, end - 1)

S = input()
n = len(S) - 1
print(isPalindrome(S, 0, n))
