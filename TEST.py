# Only for test.
n = len("abbcbba")
is_palindrome = [[False] * n for _ in range(n)]
for i in range(n):
    is_palindrome[i][i] = True
for i in range(n):
    is_palindrome[i][i - 1] = True
for i in is_palindrome:
    print(i)