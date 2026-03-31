class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_nums = {}
        frequency = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            map_nums[num] = 1 + map_nums.get(num, 0)

        for num, freq in map_nums.items():
            frequency[freq].append(num)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
        