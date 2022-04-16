# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri]. The array
# describes the questions of an exam, where you have to process the questions in order (i.e., starting from question
# 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but
# you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the
# decision on the next question.
#
# For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]: If question 0 is solved, you will earn 3 points
# but you will be unable to solve questions 1 and 2. If instead, question 0 is skipped and question 1 is solved,
# you will earn 4 points but you will be unable to solve questions 2 and 3. Return the maximum points you can earn
# for the exam.

# Example 1:
#
# Input: questions = [[3,2],[4,3],[4,4],[2,5]]
# Output: 5
# Explanation: The maximum points can be earned by solving questions 0 and 3.
# - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
# - Unable to solve questions 1 and 2
# - Solve question 3: Earn 2 points
# Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
# Example 2:
#
# Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Output: 7
# Explanation: The maximum points can be earned by solving questions 1 and 4.
# - Skip question 0
# - Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
# - Unable to solve questions 2 and 3
# - Solve question 4: Earn 5 points
# Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
#
#
# Constraints:
#
# 1 <= questions.length <= 105
# questions[i].length == 2
# 1 <= pointsi, brainpoweri <= 105

# 思路：1. recursion，for each position, we have two choices, do the quesiton or not do it. If we choose to do this
#         question, the total points we could get is the points we get from current position and the max points we could
#         get from the i+skip+1 position. If we decide not to do this question, the points we could get is the maximum
#         points from i+1 position. So each time, we need to compare with one is bigger.
#      2. We need to clarify that what helper(questions, i) return? It return the maximum points we can get for the ith
#         index.
#      3. DP: without dp, each time we come to index i, we need dfs to find the base case, then return back, the time
#         complexity is huge. So we need an additional data structure to store the maximum points we can get for each
#         position. Then we will only need to calculate the maximum points once for each position.So the Time complexity
#         would be O(N), the space complexity will also be O(N).

class Solution_1:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [-1] * len(questions)
        def helper(i):
            if i >= len(questions):
                return 0
            if dp[i] != -1:
                return dp[i]
            points, skip = questions[i][0], questions[i][1]
            dp[i] = max(helper(i+1), points+helper(i+skip+1))
            return dp[i]
        return helper(0)


# iteration
class Solution_2:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [-1] * (len(questions)+1)  # for the position of index len(questions)-1, need the position of index of
        # len(questions) to compare
        for i in range(len(questions)-1, -1, -1):
            if i+questions[i][1]+1 >= len(questions):  # If next question is not available, just need to compare the ith
                # position and i+1th position
                dp[i] = max(dp[i+1], questions[i][0])
            else:
                dp[i] = max(dp[i+1], questions[i][0]+dp[i+questions[i][1]+1])
        return dp[0]


