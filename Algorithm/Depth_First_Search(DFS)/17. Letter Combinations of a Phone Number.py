# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order. A mapping of digit to letters (just like on the telephone buttons) is
# given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = ""
# Output: []
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# 思路：1. 这是一道找所有可能组合的题，想到DFS（不知道输入的数字多长，要循环几层，想到recursion）

KEYBOARD = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
# 输入combination+[letter],就不用backtrack了，因为没改变combination
class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = []
        self.dfs(digits, 0, [], combinations)
        return combinations

    def dfs(self, digits, index, combination, combinations):
        if len(digits) == index:
            combinations.append(''.join(combination))
            return   # 出口要记得return

        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, combination + [letter], combinations)


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = []
        self.dfs(digits, 0, [], combinations)
        return combinations

    def dfs(self, digits, index, combination, combinations):
        if len(digits) == index:
            combinations.append(''.join(combination))
            return

        for letter in KEYBOARD[digits[index]]:
            combination.append(letter)
            self.dfs(digits, index + 1, combination, combinations)
            combination.pop()