# Given an array nums of size n, return the majority element. The majority element is the element that appears more
# than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1

# Follow-up: Could you solve the problem in linear time and in O(1) space?

# 思路：
# 1. collections.Counter
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        n = len(nums)
        for k, v in d.items():
            if v > n/2:
                return k

class Solution2:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
# Time complexity : O(n). We iterate over nums once and make a constant time HashMap insertion on each iteration.
# Therefore, the algorithm runs in O(n)O(n) time.
# Space complexity : O(n)
# 2. sort
class Solution3:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# 3. Boyer-Moore algorithm
# Essentially, what Boyer-Moore does is look for a suffix suf of nums where suf[
# 0]suf[0] is the majority element in that suffix. To do this, we maintain a count, which is incremented whenever we
# see an instance of our current candidate for majority element and decremented whenever we see anything else.
# Whenever count equals 0, we effectively forget about everything in nums up to the current index and consider the
# current number as the candidate for majority element. It is not immediately obvious why we can get away with
# forgetting prefixes of nums - consider the following examples (pipes are inserted to separate runs of nonzero count).

# [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]

# Here, the 7 at index 0 is selected to be the first candidate for majority element. count will eventually reach 0
# after index 5 is processed, so the 5 at index 6 will be the next candidate. In this case, 7 is the true majority
# element, so by disregarding this prefix, we are ignoring an equal number of majority and minority elements -
# therefore, 7 will still be the majority element in the suffix formed by throwing away the first prefix.

# [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]

# Now, the majority element is 5 (we changed the last run of the array from 7s to 5s), but our first candidate is
# still 7. In this case, our candidate is not the true majority element, but we still cannot discard more majority
# elements than minority elements (this would imply that count could reach -1 before we reassign candidate,
# which is obviously false).

# Therefore, given that it is impossible (in both cases) to discard more majority elements than minority elements,
# we are safe in discarding the prefix and attempting to recursively solve the majority element problem for the
# suffix. Eventually, a suffix will be found for which count does not hit 0, and the majority element of that suffix
# will necessarily be the same as the majority element of the overall array.

# 理解： 遇到当前candidate就+1，不是就-1，count=0就更新candidate，每次更新candidate相当于把前面一段数减去了，从新开始，类似recursion。
# 无论减去的candidate是不是真正的majority number，都不会造成减去更多majority number的情况，至少是一半majority，一半其他数，所以剩下
# 数中majority number不会变。
class Solution3:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

# Time complexity : O(n)
# Boyer-Moore performs constant work exactly nn times, so the algorithm runs in linear time.

# Space complexity : O(1)
# Boyer-Moore allocates only constant additional memory.
