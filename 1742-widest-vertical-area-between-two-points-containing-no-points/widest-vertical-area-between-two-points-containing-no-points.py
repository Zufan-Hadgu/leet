class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x_cordinate = []
        for i in range (len(points)):
            x_cordinate.append(points[i][0])
        x_cordinate.sort()
        l = 0
        r = 1
        vertical_dif = 0
        while r < len(x_cordinate):
            value = x_cordinate[r] - x_cordinate[l]
            if value > vertical_dif:
                vertical_dif = value
            l += 1
            r += 1
        return vertical_dif


        