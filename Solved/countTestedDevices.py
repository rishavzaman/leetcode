class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        pointer = 0
        count = 0
        L = len(batteryPercentages)
        while pointer < L:
            if batteryPercentages[pointer] > 0:
                count += 1
                for j in range(pointer+1,L):
                    batteryPercentages[j] = max(0,batteryPercentages[j]-1)
            pointer += 1
        return count