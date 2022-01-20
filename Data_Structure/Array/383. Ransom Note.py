# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false
# otherwise. Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

# 思路： 1. 第一时间想到hashmap
#       2. str 也可以用in判断是否含有某个字母

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # For each character, c,  in the ransom note.
    for c in ransomNote:
        # If there are none of c left in the String, return False.
        if c not in magazine:
            return False
        # Find the index of the first occurrence of c in the magazine.
        location = magazine.index(c)
        # Use splicing to make a new string with the characters
        # before "location" (but not including), and the characters
        #after "location".
        magazine = magazine[:location] + magazine[location + 1:]
    # If we got this far, we can successfully build the note.
    return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for i in range(len(ransomNote)):
            hashmap[ransomNote[i]] = hashmap.get(ransomNote[i], 0) + 1
        for i in range(len(magazine)):
            if magazine[i] in hashmap:
                hashmap[magazine[i]] -= 1
                if hashmap[magazine[i]] == 0:
                    hashmap.pop(magazine[i])
        if len(hashmap) == 0:
            return True
        return False