# Search In Rotated Sorted Array
from ast import List
class Partha(object):
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        
        while low<=high:
            
            mid = low + ((high - low)>>1)
            
            if nums[mid]==target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1            
        return -1
ob1 = Partha()
print(ob1.search(nums = [4,5,6,7,0,1,2], target = 0))