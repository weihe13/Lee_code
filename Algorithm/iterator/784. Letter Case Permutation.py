# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.

# Example 1:
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:
#
# Input: s = "3z4"
# Output: ["3z4","3Z4"]

# Constraints:
# 1 <= s.length <= 12
# s consists of lowercase English letters, uppercase English letters, and digits.

# 思路：If the next character c is a letter, then we will duplicate all words in our current answer, and add lowercase(
# c) to every word in the first half, and uppercase(c) to every word in the second half.
# If instead c is a digit, we'll add it to every word.

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [[]]

        for char in s:
            n = len(ans)  # 这步是关键，每次循环时重新确定n
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[i + n].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)
        return map("".join, ans)