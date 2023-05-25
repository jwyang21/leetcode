class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+nums2
        merged = sorted(merged)
        left, right = 0, len(merged)-1
        mid = (left+right)//2
        
        if len(merged)%2==0:
            median_ = (merged[mid]+merged[mid+1])/2
        else:
            median_ = merged[mid]
        return median_
        