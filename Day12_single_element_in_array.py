class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count=2
        var=nums[0]
        size=len(nums)
        if size==1:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        for i in range(size):
            if nums[i]==var and count!=0:
                count-=1
                var=nums[i]
            elif nums[i]!=var and count==0:
                count=1
                var=nums[i]
            elif nums[i]!=var and count!=0:
                return var
        return var