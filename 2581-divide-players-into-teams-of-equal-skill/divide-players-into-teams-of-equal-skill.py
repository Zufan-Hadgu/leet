class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) -1
        target_sum = skill[0] + skill[-1]
        chemistry_sum = 0

        while l <= r:
            if skill[l] + skill[r] != target_sum:
                return - 1
            chemistry_sum += skill[l] * skill[r]
            l += 1
            r -= 1
        return chemistry_sum





        