class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        di = defaultdict()
        groups = -1
        out = []
        if not nums:
            return 0
        
        nums = list(set(nums))
        for num in nums:
            
            
            if num - 1 in di:

                out[di[num - 1]].append(num)
                di[num] = di[num - 1]
            elif num + 1 in di:
                out[di[num+1]].append(num)
                di[num] = di[num + 1]
            else:
                groups += 1
                out.append([num])          
                di[num] =  groups
        
        merge = {}
        groups = 0
        for idx, group in enumerate(out):

            if max(group) + 1 in merge:
                out[merge[max(group) + 1]] = out[merge[max(group) + 1]] + out[idx]
            else:
                merge[max(group)] = idx
            if min(group) - 1 in merge:
                out[merge[max(group) - 1]] = out[merge[max(group) - 1]] + out[idx]
            else:
                merge[min(group)] = idx
            


        longest = 0
        for idx, group in enumerate(out):
            if len(group) > len(out[longest]):
                longest = idx

        return len(out[longest])
