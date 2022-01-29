def maxAZ(string):
    add_A = 'A' + string
    add_Z = string + 'Z'
    count_A = 0
    count_Z = 0

    temp = 0

    for i in range(len(add_A)):
        if add_A[i] == 'Z':
            count_A += temp
        if add_A[i] == "A":
            temp += 1

    temp_ = 0
    for i in range(len(add_Z)):
        if add_Z[i] == 'Z':
            count_Z += temp_
        if add_Z[i] == "A":
            temp_ += 1
    return max(count_A, count_Z)

# print(maxAZ("A")) #1
# print(maxAZ("BAZAZ")) #5

def findEarliestMonth(stockPrices):
    total1 = 0
    total2 = sum(stockPrices)
    month = 0
    min_ = float("inf")
    for i in range(len(stockPrices) - 1):
        total1 += stockPrices[i]
        total2 -= stockPrices[i]
        avg_1 = total1 // (i + 1)
        avg_2 = total2 // (len(stockPrices) - 1 - i)
        diff = abs(avg_1 - avg_2)
        if diff < min_:
            min_ = diff
            month = i + 1

    return month


# print(findEarliestMonth([1,3,2,3])) #2

def getEncryptedNumber(array):
    level = array
    while len(level) > 2:
        temp = []
        for i in range(len(level) - 1):
            temp.append(int(str(level[i] + level[i + 1])[-1]))
        level = temp
    return level


# print(getEncryptedNumber([1,2,3,4])) #82
# print(getEncryptedNumber([4,5,6,7])) #04

def maxSpread(levels, maxspread):
    levels.sort()
    curr = levels[0]
    count = 1
    for i in range(len(levels)):
        if levels[i] > curr + maxspread:
            count += 1
            curr = levels[i]
    return count


# print(maxSpread([1, 4, 7, 3, 4], 2))  # 3
# print(maxSpread([3, 2, 1, 4, 7], 2))  # 3
# print(maxSpread([4, 4, 1, 8, 7], 2))  # 3
def commonPrefix(string):
    # z-array
    z = [0] * len(string)
    z[0] = len(string)
    left, right = 0,0
    for i in range(1, len(string)):
        if i <= right:
            z[i] = min(z[i-left], right-i+1)
        while i+z[i] < len(string) and string[z[i]] == string[z[i]+i]:
            z[i] += 1
        if i+z[i]-1 > right:
            left = right
            right = i+z[i]-1
    return sum(z)

# print(commonPrefix('ababaa')) #11
# print(commonPrefix('aa')) #3
def getMaxValue(list_):
    list_.sort()
    list_[0] = 1
    for i in range(1, len(list_)):
        if list_[i] > list_[i-1]:
            list_[i] = list_[i-1]+1
    return list_[-1]
#
# print(getMaxValue([3,1,3,4])) #4
# print(getMaxValue([1,3,2,2])) #3
# print(getMaxValue([3,2,3,5])) #4
def kOddElements(arr, k):
    res = set()
    left, right, odd_num = 0, 0, 0
    while right < len(arr):
        if arr[right] % 2 == 1:
            odd_num += 1
        while odd_num > k and left < right:
            if arr[left] % 2 == 1:
                odd_num -= 1
            left += 1

        for left_start in range(left, right + 1):
            res.add(",".join(map(str, arr[left_start:right + 1])))

        right += 1

    return len(res)


# print(kOddElements([3,2,3,4], 1)) #7
# print(kOddElements([1,3,9,5], 2)) #7
# print(kOddElements([3,2,3,2], 1)) #5
# print(kOddElements([2, 2, 5, 6, 9, 2, 11, 9, 2, 11, 12], 1)) #18
# print(kOddElements([1,2,3,4], 1)) #8

def maxSubjectsNumber(needed, answered, q):
    still_need = []
    for i in range(len(needed)):
        still_need.append(needed[i] - answered[i])
    print(still_need)
    still_need.sort()
    count = 0
    for i in range(len(still_need)):
        if q <= 0:
            break
        if still_need[i] < 0:
            count += 1
        else:
            if q >= still_need[i]:
                q -= still_need[i]
                count += 1
    return count

# print(maxSubjectsNumber([51,52,100], [24,27,0], 100))
def merge(intervals):
    intervals.sort()
    res = []
    for i in range(len(intervals)):
        if not res or res[-1][1] < intervals[i][0]:
            res.append(intervals[i])
        else:
            res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]

    return res
# print(merge([[6,9],[2,3],[9,11],[1,5],[14,18]]))
def kthFactor(n, k):
    divisors, sqrt_n = [], int(n ** 0.5)
    for x in range(1, sqrt_n + 1):
        if n % x == 0:
            k -= 1
            divisors.append(x)
            if k == 0:
                return x
    if (sqrt_n * sqrt_n == n):
        k += 1

    if k <= len(divisors):
        return n // divisors[len(divisors) - k]
    else:
        return 0
# print(kthFactor(20,3))
# print(kthFactor(20,7))
def countMaximumTeams(arr, teamSize, maxDiff):
    arr.sort()
    answer = 0
    i = 0
    while i <= len(arr) - teamSize:
        if arr[i+teamSize-1] - arr[i] <= maxDiff:
            answer += 1
            i += teamSize
        else:
            i += 1
    return answer

# print(countMaximumTeams([3,4,3,1,6,5], 3,2)) #2
import collections
def firstUniqueCharacter(s):
    count = collections.Counter(s)
    print
    for index, each in enumerate(s):
        if count[each] == 1:
            return index
    return -1

# print(firstUniqueCharacter("leetcode")) #0
# print(firstUniqueCharacter("loveleetcode")) #2
# print(firstUniqueCharacter("aabb")) #-1
def sumOfSubarrayRanges(A):
    res = 0
    n = len(nums)
    for i in range(n):
        l, r = nums[i], nums[i]
        for j in range(i+1, n):
            l = min(l, nums[j])
            r = max(r, nums[j])
            res += r - l
    return res

    # res = 0
    # inf = float('inf')
    # A = [-inf] + A0 + [-inf]
    # s = []
    # for i, x in enumerate(A):
    #     while s and A[s[-1]] > x:
    #         j = s.pop()
    #         k = s[-1]
    #         res -= A[j] * (i - j) * (j - k)
    #     s.append(i)
    #
    # A = [inf] + A0 + [inf]
    # s = []
    # for i, x in enumerate(A):
    #     while s and A[s[-1]] < x:
    #         j = s.pop()
    #         k = s[-1]
    #         res += A[j] * (i - j) * (j - k)
    #     s.append(i)
    # return res

# print(sumOfSubarrayRanges([1,2,3])) #4
# print(sumOfSubarrayRanges([1,3,3])) #4
# print(sumOfSubarrayRanges([4,-2,-3,4,1])) #59
def sumOfMinimumsInSubarrays(A):
    res = 0
    stack = []  # non-decreasing
    A = [float('-inf')] + A + [float('-inf')]
    for i, n in enumerate(A):
        while stack and A[stack[-1]] > n:
            cur = stack.pop()
            res += A[cur] * (i - cur) * (cur - stack[-1])
        stack.append(i)
    return res % (10 ** 9 + 7)

import math
def maximumQuality(packets, channels):
    packets.sort()
    answer = 0
    non_single = len(packets) - channels + 1
    answer = sum(packets[:non_single]) / len(packets[:non_single])
    for i in range(non_single, len(packets)):
        answer += packets[i]

    return answer

# print(maximumQuality([1,2,3,4,5], 2))
# print(maximumQuality([5,2,2,1,5,3], 2))

def minKeyboardClick(string):
    string = list(string)
    answer = 0
    count = list(collections.Counter(string).keys())
    for i in range(len(string)):
        if 0 <= count.index(string[i]) < 9:
            answer += 1
        elif 9 <=  count.index(string[i]) < 18:
            answer += 2
        elif 18 <=  count.index(string[i]) < 27:
            answer += 3

    return answer

# print(minKeyboardClick('abcdefgabc')) #10
# print(minKeyboardClick('hellooooo')) #9
# print(minKeyboardClick('hhheelloooooabcdefgopqrst')) #31

def maxConsecutiveOnes(nums, k):
    left = 0
    ans = []
    for right in range(len(nums)):
        k -= 1 - nums[right]
        if k < 0:
            k += 1 - nums[left]
            left += 1

    for i in range(left, right):
        if nums[i] == 0:
            ans.append(i)
    return ans

# print(maxConsecutiveOnes([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],2)) #[5, 7]
# print(maxConsecutiveOnes([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],1)) #[7]
# print(maxConsecutiveOnes([0, 0, 0, 1],4)) #[0, 1 ,2]
def findMinimumCharacter(searchWord, resultWord):
    p1, p2 = 0, 0
    n1, n2 = len(searchWord), len(resultWord)
    while p1 < n1 and p2 < n2:
        if searchWord[p1] == resultWord[p2]:
            p2 += 1
        p1 += 1
    return n2 - p2
# print(findMinimumCharacter("armaze", "amazon")) #2

def s_t(s, t):
    count_s = collections.Counter(s)
    count_t = collections.Counter(t)
    min_ = float("inf")
    for i in range(len(t)):
        min_ = min(min_, math.floor(count_s[t[i]] / count_t[t[i]]))
    return min_

# print(s_t('mononom', "mon")) #2

def validString(string):
    stack = []
    for i in range(len(string)):
        if not stack or stack[-1] != string[i]:
            stack.append(string[i])
        else:
            stack.pop()

    return len(stack) == 0
# print(validString("vv")) #true
# print(validString("xbbx")) #true
# print(validString("bbccdd")) #true
# print(validString("xyffyxdd")) #true

def passwordStrength(string):
    last = {chr(97+i): -1 for i in range(26)}
    ret = 0
    for index, char in enumerate(string):
        left = index - last[char]
        right = len(string) - index
        ret += left * right
        last[char] = index
    return ret

# print(passwordStrength("good")) #16
# # # print(passwordStrength("test")) #19
# # # print(passwordStrength("abc")) #10
def simpleCipher(encrypted, k):
    k = k % 26
    answer = ""
    for i in range(len(encrypted)):
        value = ord(encrypted[i]) - ord("A") - k
        if value < 0:
            value += 26
        value += ord("A")
        answer += chr(value)
    return answer
# print(simpleCipher("VTAOG", 2)) #TRYME

def encodeString(s):
    answer = [0] * 26
    number_of_repetation = 0
    i = len(s) - 1
    while i >= 0:
        number_of_repetation = 0
        if s[i] == ')':
            go_back = i - 1
            multipliy = 1
            while go_back >= 0 and s[go_back] != '(':
                number_of_repetation += multipliy * int(s[go_back])
                go_back -= 1
                multipliy *= 10
            i = go_back - 1
        # in case of '#' then I have to go back two steps to get first digt *10 and the second digit
        if s[i] == '#':
            expected_number = (int(s[i - 2])) * 10 + int(s[i - 1])
            # May there be a ()
            if number_of_repetation == 0:
                answer[expected_number - 1] += 1
            else:
                answer[expected_number - 1] += number_of_repetation
            i -= 3
            continue
        if number_of_repetation == 0:
            answer[int(s[i]) - 1] += 1
        else:
            answer[int(s[i]) - 1] += number_of_repetation

        i -= 1
    return answer

# print(encodeString("1226#24#")) #abzx
# print(encodeString("1(2)23(3)")) #aabccc
# print(encodeString("2110#(2)")) #bajj
# print(encodeString("23#(2)24#25#26#23#(3)")) #wwxyzwww
#

def badNumbers(lower, upper, nums):
    #missing ranges
    result = []
    prev = lower - 1
    for i in range(len(nums) + 1):
        if i < len(nums):
            curr = nums[i]
        else:
            curr = upper + 1
        if prev + 1 <= curr - 1:
            if prev + 1 == curr - 1:
                result.append(str(prev + 1))
            else:
                result.append(str(prev + 1) + "->" + str(curr - 1))
        prev = curr
    return result


def maxValue(length, updates):
    #370 range addition
    answer = [0]*length
    ans = [0] * length
    for start, end, value in updates:
        ans[start] += value
        end += 1
        if end < len(ans):
            ans[end] -= value

    for i in range(1, len(ans)):
        ans[i] += ans[i - 1]

    return ans



def dailyTemp(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and stack[-1][0] < temperatures[i]:
            temperature, index = stack.pop()
            answer[index] = i - index
        stack.append([temperatures[i], i])
    return answer
# print(dailyTemp([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
def maxProfit(arr, k):
    n = len(arr)
    maxProfit = float('-inf')
    # Evaluate all n/2 harvesting options (6 slices->3 options, 4 slices->2 options, and so on)
    for i in range(n // 2):
        sm = 0
        for j in range(k):
            currIndex = i + j
            oppositeIndex = (currIndex + (n // 2)) % n  # adding n//2 gets us the opposite slice's index. %2 for wrapping around array
            sm += arr[currIndex] + arr[oppositeIndex]
        maxProfit = max(maxProfit, sm)

    return maxProfit


# print(maxProfit([1, 5, 1, 3, 7, -3], 2)) #16
# # print(maxProfit([-6, 3, 6, -3], 1)) #0
# # print(maxProfit([3, -5], 1)) #-2
def countBinarySubstrings(s):
    groups = [1]
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            groups.append(1)
        else:
            groups[-1] += 1
    ans = 0
    for i in range(1, len(groups)):
        ans += min(groups[i], groups[i-1])
    return ans


# print(countBinarySubstrings("00110011")) #6
def minSwaps(s):
    start_with_one = start_with_zero = 0
    count_one = count_zero = 0

    for c in s:
        if c == 0:
            start_with_zero += count_one
            count_zero += 1
        else:
            start_with_one += count_zero
            count_one += 1

    return min(start_with_zero, start_with_one)
# print(minSwaps([0,1,0,1])) #1
# print(minSwaps([1,1,0,1])) #1
def getMaximumGrey(grid):
    row = [0] * len(grid)
    col = [0] * len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                row[i] += 1
            else:
                row[i] -= 1

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i] == "1":
                col[i] += 1
            else:
                col[i] -= 1

    return max(row) + max(col)

# print(getMaximumGrey(["101", "001", "110"]))
def maximumAverageSubtree(self, root):
    self.res = 0

    def helper(root):
        if not root: return [0, 0.0]
        n1, s1 = helper(root.left)
        n2, s2 = helper(root.right)
        n = n1 + n2 + 1
        s = s1 + s2 + root.val
        self.res = max(self.res, s / n)
        return [n, s]

    helper(root)
    return self.res
def min_roof(arr, k):
    arr.sort()
    min_ = float('inf')
    for i in range(len(arr)-k):
        min_ = min(min_, arr[i+k-1]-arr[i]+1)
    return min_


# print(min_roof([12,6,5,2],3)) #5
# print(min_roof([12,6,5,2,9],4)) #8
def decode(string, n):
    matrix = [[0]*(len(string)//3) for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(len(string)//3):
            matrix[i][j] = string[index]
            index += 1
    answer = ""
    for i in range(len(string)//3):
        x = 0
        while (x < n and i < len(string)//3):
            if (matrix[x][i] == '_'):
                answer += ' '
            else:
                answer += matrix[x][i]
            x += 1
            i += 1

    return answer

# print(decode("mnesi___ya__k____mime", 3)) #my name is mike

#992. Subarrays with K Different Integers
def subarraysWithKDistinct(A, K):
    return atMostK(A, K) - atMostK(A, K - 1)


def atMostK(A, K):
    count = collections.Counter()
    res = i = 0
    for j in range(len(A)):
        if count[A[j]] == 0: K -= 1
        count[A[j]] += 1
        while K < 0:
            count[A[i]] -= 1
            if count[A[i]] == 0: K += 1
            i += 1
        res += j - i + 1
    return res
# print(subarraysWithKDistinct([1,2,1,2,3], 2))
#7; [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
#1481. Least Number of Unique Integers after K Removals
def findLeastNumOfUniqueInts(arr, k):
        from collections import Counter
        count = sorted(Counter(arr).items(), key = lambda x:x[1])
        print(count)
        removed = 0  # number of removed items
        for key, val in count:
            if k >= val:
                k -= val
                removed += 1
            else:
                break
        return len(count)-removed  # number of remained elements
# print(findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))

#给一组数组, 删掉k个连续元素, 问剩下最小的和是多少?
def deleteK(arr, k):
    min_ = float("inf")
    left = 0
    right = k
    sum_ = sum(arr) - sum(arr[left:right])
    min_ = sum_
    while right < len(arr):
        sum_ += arr[left] - arr[right]
        min_ = min(min_, sum_)
        left += 1
        right += 1
    return min_
# print(deleteK([7,3,6,1], 2)) #7

def find_min_cluster(bootingPower, processingPower, powerMax):
    process = [processingPower[0]]
    for i in range(1, len(processingPower)):
        process.append(process[i-1] + processingPower[i])
    k = len(processingPower)
    while k > 0:
        net_power_consumption = 0
        left = 0
        right = k - 1
        while right < len(processingPower):
            if left == 0:
                net_power_consumption = max(bootingPower[left:right]) + k * process[right]
            else:
                net_power_consumption = max(bootingPower[left:right]) + k*(process[right]-process[left])

            print(net_power_consumption)

            if net_power_consumption <= powerMax:
                return k
            right += 1
            left += 1
        k -= 1

    return 0
# print(find_min_cluster([3,6,1,3,4], [2,1,3,4,5], 25)) #3
def weights(arr):
    count = collections.Counter(arr)
    remove = 0
    for key in count:
        if count[key] % 3 == 0:
            remove += count[key] // 3
        elif count[key] % 3 == 2:
            remove += count[key] // 3
            remove += 1
        elif count[key] % 3 == 1:
            if count[key] % 2 == 0:
                remove += (count[key]-4)//3
                remove += 2

            return -1
    return remove


# print(weights([2,2,2,3,3,5,5,5,5,5,5])) #4
# # # # # print(weights([1,2,3,4])) #-1
# # # # # print(weights([4,4,4,4,4,4,4,4])) #3
def findDataLocations(locations, moveFrom, moveTo):
    for i in range(len(moveFrom)):
        locations[locations.index(moveFrom[i])] = moveTo[i]
    return sorted(locations)
# print(findDataLocations([1,7,6,8], [1,7,2], [2,9,5])) #[5,6,8,9]

def findMamimumSum(arr, k):
    max_ = float('-inf')
    for i in range(len(arr)-k+1):
        if len(set(arr[i:i+k])) == 3:
            max_ = max(max_, sum(arr[i:i+k]))
    return max_
# print(findMamimumSum([1,2,7,7,4,3,6], 3)) #14