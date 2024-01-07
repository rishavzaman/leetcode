class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for i, p in enumerate(groupSizes):
            if p not in dic:
                dic[p] = [i]
            else:
                dic[p].append(i)
        
        groups = []
        for k in dic:
            if len(dic[k]) > k:
                tmp = dic[k]
                for i in range(0, len(tmp), k):
                    groups.append(tmp[i:i+k])
            else:
                groups.append(dic[k])


        return groups

        # groupsizes = [3,3,3,3,3,1,3]
        # dic == [3:[0,1,2,3,4,6], 1:[5]]
        # len(dic[3]) == 6 > 3
        # i = 0 to 5 in steps of 3
        # i = 0, i = 3, 
        # groups.append(tmp[0:3]), groups.append(tmp[3:6])