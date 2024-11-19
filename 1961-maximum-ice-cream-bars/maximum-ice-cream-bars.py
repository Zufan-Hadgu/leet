class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        count = 0
        summ = 0
        for i in range (len(costs)):
            summ = summ + costs[i]
            if summ <= coins:
                count += 1
        return count

