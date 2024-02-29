#given a sorted array, find an element using binary search
#find the middle element; if the middle element is bigger than the element, go to the left (0, n/2)
#if the element is bigger than the element, go to the right (n/2+1, n)
#if the element is equal, return

def binarySearch(arr, x):
	start, end = 0, len(arr)-1
	while start <= end:
		middle = (start+end) // 2
		if arr[middle] == x:
			string = str(x) + " found at index " + str(middle)
			return string
		elif arr[middle] > x:
			end = middle -1
		else:
			start = middle +1


def binary_search(arr, x):
	return binary_search_recursive(0, len(arr)-1, x, arr)


def binary_search_recursive(start, end, x, arr):
	middle = (start+end)//2
	if arr[middle] == x:
		string = str(x) + " found at index " + str(middle)
		return string
	elif arr[middle] > x:
		return binary_search_recursive(start, middle-1, x, arr)
	else:
		return binary_search_recursive(middle+1, end, x, arr)



# Test array
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7
 
# Function call
result = binarySearch(arr, x)
print(result)
 
