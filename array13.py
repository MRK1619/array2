#Find Minimum In Rotated Sorted Array
class Partha(object):
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start)// 2
            if nums[mid] >= nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
#call The function   
ob1 = Partha()
print(ob1.findMin([11,13,15,17]))