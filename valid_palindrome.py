"""
LEETCODE #125: Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower() #make everything lowercase, O(n)
    s =''.join(e for e in s if e.isalnum()) #removing all nonalphanumeric characters, O(n)

    i,j = 0, len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("Appa"))
print(isPalindrome("aracecar"))

"""
Runtime: O(n + n + n) = O(3n) ~ O(n) #Linear time
"""