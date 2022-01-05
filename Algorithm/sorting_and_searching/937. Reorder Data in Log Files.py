# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the
# identifier. There are two types of logs: Letter-logs: All words (except the identifier) consist of lowercase
# English letters. Digit-logs: All words (except the identifier) consist of digits. Reorder these logs so that: The
# letter-logs come before all digit-logs. The letter-logs are sorted lexicographically by their contents. If their
# contents are the same, then sort them lexicographically by their identifiers. The digit-logs maintain their
# relative ordering. Return the final order of the logs.

# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
# Example 2:
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

# Constraints:
# 1 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# All the tokens of logs[i] are separated by a single space.
# logs[i] is guaranteed to have an identifier and at least one word after the identifier.

# 思路：1. We can sort tuples or other objects based on one element or feature by using sorted(key = ).
#      2. 可以用isalpha()判断一个string是否全是alphabetic, isalnum()可以判断是否全是字母或数字(AKA，不含标点符号);
#         必须判断content[0]是否是字母，因为如果第一个element只是1个字母，那么content[1]就是空格
#      3. 通过设置max split = 1可以将identifier和content区分开
#      4. sorted with key的用法：(如果Descending，sorted(a, key = a[0], reverse=True))

#         1) A common pattern is to sort complex objects using some of the object’s indices as keys.
# >>> student_tuples = [
# ...     ('john', 'A', 15),
# ...     ('jane', 'B', 12),
# ...     ('dave', 'B', 10),
# ... ]
# >>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# >>> class Student:
# ...     def __init__(self, name, grade, age):
# ...         self.name = name
# ...         self.grade = grade
# ...         self.age = age
# ...     def __repr__(self):
# ...         return repr((self.name, self.grade, self.age))
#
# >>> student_objects = [
# ...     Student('john', 'A', 15),
# ...     Student('jane', 'B', 12),
# ...     Student('dave', 'B', 10),
# ... ]
# >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

#             2) Both list.sort() and sorted() have a key parameter to specify a function (or other callable) to be
#             called on each list element prior to making comparisons.
#
# >>> sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
