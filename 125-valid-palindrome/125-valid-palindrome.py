class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()

        # remove all non-alphanumeric character
        ans = ''
        for i in range(len(s)):
            if ord(s[i]) in range(ord('a'), ord('z') + 1) or ord(s[i]) in range(ord('0'),ord('9') + 1):
                ans += s[i]
        
        if len(ans) == 1:
            return True

        # check if the phrase is palindrome
        forward = ans[:]
        backward = ans[::-1]
        if forward == backward:
            return True
        else:
            return False
        