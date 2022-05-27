#Find The Kth Largest Element
#First Sort The Array Then Find The Kth largest element
class Largest(object):
    def findKthLargest(self, nums, k):
      nums.sort()
      if k ==1:
         return nums[-1]
      temp = 1
      return nums[len(nums)-k]
ob1 = Largest()
print(ob1.findKthLargest([2,5,1,3,6,4,7,8], 5))