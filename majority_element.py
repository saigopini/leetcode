"""
LEETCODE #169: Find Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

def majority_element(nums):
	"""
	:type nums: List[int]
	:rtype: int 
	"""

	"""
	#with O(n) (linear) space
	max_value, max_count = 0, 0

	hashmap = dict()
	for i in range(len(nums)):
		if nums[i] not in hashmap:

			hashmap[nums[i]] = 1

		else:
			hashmap[nums[i]] += 1

		if hashmap[nums[i]] > max_count:
			max_count = hashmap[nums[i]]
			max_value = nums[i]

	return hashmap, max_value
	"""

	#SOLUTION 2: with O(1) constant space

	#Boyer-Moore Algorithm
	"""
	This is the idea that the majority has to occur more than half the times in the array
	because it is the majority. 
	"""
	
	max_value, max_count = 0, 0
	for n in nums:
	    if max_count == 0:
	        max_value = n
	    if n == max_value:
	        max_count += 1
	    else:
	        max_count -= 1
	return max_value

	#SOLUTION 3

	#using the idea that the majority will take up len(nums), so thus the middle element should be the majority
	#Time Complexity: O(nlogn)
	#Space Complexity O(1)

	"""
	max_value, max_count = 0, 0
	nums = sorted(nums)
	return (nums[int(len(nums)//2)])
	"""


print(majority_element([1,1,2,2,3,3,3,3,4]))
	