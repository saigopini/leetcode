#two sum
#find all two integers in an array that sum to 0

def twoSumInefficient(arr, target):
	result = []
	for i in range(0, len(arr)):
		for j in range(i+1, len(arr)):
			complement = target - arr[i]
			if arr[j] == complement:
				result.append((arr[i], arr[j]))

	return result

def twoSum(arr, target):
	result = []
	hashmap = dictionary()
	for i in range(0, len(arr)):
		index = arr[i]
		hashmap[index] = i
	for i in range(len(nums)):
		

def twoSum(arr):
	result = []
	arr = sorted(arr)

	for i in range(0, len(arr)):
		#binary search
		#use binary search to find the negative of this element
		x = (-1) * arr[i]
		start = i
		end = len(arr) - 1
		while start <= end:
			middle = (start + end) // 2
			if arr[middle] == x:
				result.append({arr[i], arr[middle]})
			elif arr[middle] > x:
				end = middle - 1
			else:
				start = middle + 1
	return result



arr = [0, 1, 2, -2, -1, 3, 4, -4]
print(twoSumInefficient(arr,0))