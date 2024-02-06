"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)
    start, end = 0, len(s)-1
    while start <= end:
        if s[start] == "-":
            return False
        elif s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

print(isPalindrome(-121))
print(isPalindrome(121))

"""
Runtime: O(n) = O(n) #Linear time
Space: O(1) #Constant Space
"""
            
    