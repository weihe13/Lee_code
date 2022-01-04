# I recently particiated on OA and I couldn't find a solution for this. It's relatively simple but I need to practice
# more :-(

# The Amazon Kindle Store is an online e-book store where readers can choose a book from a wide range of categories.
# It also provides the ability to bookmark pages the user wishes to return to later. A book is represented as a
# binary string having two types of pages:
# '0': an ordinary page
# '1': a bookmarked page
# Find the number of ways to select 3 pages in ascending index order such that no two adjacent selected pages are of
# the same type.

# Example
# book = '01001'
# The following sequences of pages match the criterion:
# [1, 2 ,3], that is, 01001 → 010.
# [1, 2 ,4], that is, 01001 → 010.
# [2, 3 ,5], that is, 01001 → 101.
# [2, 4 ,5], that is, 01001 → 101.
# The answer is 4.
# Function Description
# Complete the function numberOfWays in the editor below.
# numberOfWays has the following parameter:
# string book: a string that represents the pages of the book
# Returns
# long: the total number of ways to select 3 pages that meet the criterion

# Constraints

# 1 ≤ | book | ≤ 2 · 105
# Each character in book is either '0' or '1'.
# Sample Case 0
# Sample Input For Custom Testing
# STDIN FUNCTION
# 10111 → book = "10111"
# Sample Output
# 3
# Explanation
# The following sequences of pages match the criterion:
# [1, 2 ,3], that is, 10111 → 101.
# [1, 2 ,4], that is, 10111 → 101.
# [1, 2 ,5], that is, 10111 → 101.
#
# Sample Case 1
# Sample Input For Custom Testing
# STDIN FUNCTION
# 0001 → book = "0001"
# Sample Output
# 0
# Explanation
# It is not possible to pick a sequence of 3 pages that satisfies the conditions.


# 思路： https://leetcode.com/discuss/interview-question/1488281/Amazon-OA
#       1. 关键是不要求连续三个数字
#       2. 每次移动位置，先改right，计算answer，再改left
#       3. code更简单方法：Note that the 3-page seq's are not continuous. In my code, n0 and n1 store the number of 1-char
# sequences ending in 0 and 1 seen so far. s0 & s1 store the same of 2-char valid seq's '10' and '01'. We add the new
# valid 3-char seq's to ans. We are looping through string s. At each index i, we update ans, s0/s1, n0/n1: Update
# ans by adding num. of the new 3-char sequences. So, if s[i] == '1', we add the number s0 to ans, because it's the
# number of sequences '10' AND it equals to the num. of the new '101' sequences formed with s[i] at the end. if s[i]
# == '0', we add the number s1 to ans, because it's the number of sequences '01' AND it equals to the num. of the new
# '010' sequences formed with s[ i] at the end. Update the number of the 2-char seq's. Add new 2-char seq's formed by
# adding s[i] to 1-char seq's. Update s0 and s1 from n1 and n0 respectively. E.g. s0 += n1. We form new 2-char seq 10
# from all the 1's we've seen so far. Update the number of 1's or 0's depending on the value of s[i], a.k.a 1-char
# seq's.
#
# E.g. 11101
# At i=3 and s[i]=0, n1=3, n0=0, s0=s1=0.
# We calculate ans += s1, which makes ans=0; there are no 3-char seqs.
# s0 += n1, because we form new seq's '10' by adding s[i]=0 at the end of n1's
# n0 += 1
# At i=4 and s[i]=1, ans += s0

def number_of_ways(s:str)-> int:
    left = {'0': 0, '1': 0}
    right = {'0': s.count('0')}
    right['1'] = len(s) - right['0']
    answer = 0
    for c in s:
        right[c] -= 1
        if c == '1':
            answer += left['0'] * right['0']
        else:
            answer += left['1'] * right['1']
        left[c] += 1
    return answer

tests = [
    ['01001', 4],
    ["10111", 3],
    ["0001", 0]
]


for s, expected in tests:
    result = number_of_ways(s)
    print(result, expected)
    assert result == expected

def numberOfWays(s: str):
    ans = 0
   # n0,n1 - number 0's,1's so far
   # s0,s1 - number 2-combinations ending in 0's,1's
    n0 = n1 = s0 = s1 = 0
    for ch in s:
        if ch == '1':
            ans += s0
            s1 += n0
            n1 += 1
        else:  # ch '0'
            ans += s1
            s0 += n1
            n0 += 1
    return ans