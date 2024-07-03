'''350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 '''


nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
nums1.sort()
nums2.sort()
i=0
j=0
res=[]
while i<len(nums1) and j<len(nums2):
    if nums1[i]==nums2[j]:
        res.append(nums1[i])
        i=i+1
        j=j+1
    elif nums1[i]<nums2[j]:
        i=i+1
    elif nums1[i]>nums2[j]:
        j=j+1
print(res)