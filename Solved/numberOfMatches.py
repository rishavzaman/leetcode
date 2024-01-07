class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n
        count = 0
        while teams > 1:
            if teams % 2 == 0:
                count += teams // 2
                teams = teams // 2
            else:
                count += (teams - 1) // 2
                teams = (teams - 1) // 2 + 1
        return count