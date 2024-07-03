'''Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.'''

#method 1
nums1 = [1,2,2,1]
nums2 = [2,2]
res=list(set(nums1).intersection(set(nums2)))
print(res)

#method 2
res1=[]
for i in nums1:
    if i in nums2:
        res1.append(i)
print(list(set(res1)))
