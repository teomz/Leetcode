class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            # you can get 0 if all values are positive
            if nums[i] > 0:
                break
            # duplication will be skip 
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            left = i+1
            right = len(nums)-1
            while left < right:    
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -= 1
                    # skip duplication
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return output
                
                

                            
        
                

                            
        