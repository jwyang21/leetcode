class Solution:
    #https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/746975/python-3find-first-and-last-position-search-for-a-range/
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        ending = -1
        
        high = len(nums)-1
        low = 0
        
        if len(nums)==1:
            if target in nums:
                return [0,0]
            else:
                return [-1,-1]
            
        # find start   
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                start = mid
                high = mid-1 #search left subspace
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1 #search right subspace
        
        # find ending
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                ending = mid
                low = mid+1 #search right subspace
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
                
        
        return [start, ending]