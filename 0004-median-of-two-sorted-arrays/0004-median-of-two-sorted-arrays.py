class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = nums1 + nums2
        array = sorted(array)

        return float(array[len(array)//2]) if len(array)%2 != 0 else (array[int(len(array)/2)] + array[int(len(array)/2)-1])/2.0
