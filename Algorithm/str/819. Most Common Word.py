# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not
# banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique. The words in
# paragraph are case-insensitive and the answer should be returned in lowercase.

# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"

# Constraints:
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.

# 思路：1. lower case
#      2. 考虑怎么去除标点符号，比如'ball,'和'ball'，自己想到的是replace，更方便的是isalnum和re.split
#      3. 注意用split去除. ? ' 时，要在前加'\'。

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        #2). split the string into words
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        #3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        #4). return the word with the highest frequency
        return max(word_count.items(), key=operator.itemgetter(1))[0]

#用re.split()，思路巧妙一些，速度较快，可以超过100%
        import re
        paragraph = paragraph.lower()
        paragraph = re.split("; |, |,| |! |!|\'|\? |\.|\. ", paragraph)
        count = Counter(paragraph)
        sort = count.most_common()
        banned = [s.lower() for s in banned]
        for i in sort:
            if i[0] in banned or i[0] == '':
                continue
            else:
                return i[0]
