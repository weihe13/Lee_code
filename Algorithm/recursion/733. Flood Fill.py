# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the
# image.You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting
# from the pixel image[sr][sc].To perform a flood fill, consider the starting pixel, plus any pixels connected
# 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected
# 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with newColor.Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2 Output: [[2,2,2],[2,2,0],[2,0,
# 1]] Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels
# connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2 Output: [[2,2,2],[2,2,2]]

# Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 216
# 0 <= sr < m
# 0 <= sc < n

# 思路：看完题第一反应是用recursion，但是细节还有几个地方要注意：
#      1. 需要先判断color == newColor的情况，直接return image，否则会一直循环下去。
#      2. 这种对上层函数的输入参数原位修改的情形，不用把修改对象作为参数再输入给下层修改函数。
#      3. 这种原位修改的函数，最后不需要return，在recursion时也不能return，直接call。
#      4. 注意recursion条件判断的写法，自己写时也考虑到了边界问题，但是想的是一起考虑，没有想到分成四种情况。
#      5. recursion条件判断时，注意len(image)是tr，能取到的最大行位置是tr-1,所以判断条件是r+1<=tr-1。
#      6. 为什么这里image不用 nonlocal，因为是list

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        tr, tc = len(image), len(image[0])

        if color == newColor: return image

        def findpix(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: findpix(r - 1, c)
                if r + 1 <= tr - 1: findpix(r + 1, c)
                if c >= 1: findpix(r, c - 1)
                if c + 1 <= tc - 1: findpix(r, c + 1)

        findpix(sr, sc)
        return image

