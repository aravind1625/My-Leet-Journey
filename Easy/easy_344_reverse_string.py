need to reverse the array of characters in a given input string\
Input: s = ["h","e","l","l","o"]\
Output:s = ["o","l","l","e","h"]
```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i = i+1
            j = j-1
```
