# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style
# file system, convert it to the simplified canonical path. In a Unix-style file system, a period '.' refers to the
# current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (
# i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are
# treated as file/directory names.

# The canonical path should have the following format:
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.

# The path only contains the directories on the path from the root directory to the target file or directory (i.e.,
# no period '.' or double period '..') Return the simplified canonical path.

# Example 1:
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
# Example 2:
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
# Example 3:
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

# Constraints:
#
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.

# 思路：1. Different directories will be seperated by '/', think of split. If we don't use split, use a for loop to
#         iterate the input string instead, we will meet several corner cases. For example, '../.....//ab',
#         in this case we need to continuously check the next index after we encounter a '.'.
#      2. One thing to pay attention is the result should start with '/', but do not add '' or '/' into the stack.
#         maintain the stack to be empty at beginning, and add '/' when return the result. Otherwise, it may produce
#         other bugs.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')
        for p in paths:
            if p == '.' or not p:  # also need to check whether p is ''(produced by split), otherwise, it will produce
                # multiple '///' in the result.
                continue
            elif p == '..' and len(stack) >= 1:
                stack.pop()
            elif p == '..':  # 没有这个判断，如果第一个就是'..', it will be added to the stack
                continue
            else:
                stack.append(p)
        return '/'+'/'.join(stack)