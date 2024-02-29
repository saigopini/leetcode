class ElementarySorting:
    def __init__(self, arr):
        self.array = arr
    """
    Selection Sort: find the min value from i to the end and swap it with element in i
    Time: O(n^2)
    Space: O(1)
    """   
    def selectionSort(self):
        for i in range(len(self.array)):
            minIndex = i
            minValue = self.array[i]
            swapValue = self.array[i]
            for j in range(i, len(self.array)):
                if self.array[j] < minValue:
                    minValue = self.array[j]
                    minIndex=j
            self.array[i], self.array[minIndex] = minValue, swapValue
        print(self.array)

    """
    Insertion sort: if the current element is less than the element to it's left ofit
    keep swaping to its left until it's not
    Time Complexity
        BEST CASE: partially sorted or fully sorted: O(n)
        WORST CASE: O(n^2)
    Space:
        O(1)
    
    """
    
    def insertionSort(self):
        i, j = 1,1
        for i in range(1, len(self.array)):
            j = i
            prev = i-1
            while array[j] < self.array[prev] and j >= 0 and prev >=0:
                self.array[j], self.array[prev] = self.array[prev], array[j]
                j = prev
                prev = j - 1
        print(self.array)
    

array = [8,9,1,2,3,5,6,0,10,4,6,7]
s = ElementarySorting(array)
s.insertionSort()

