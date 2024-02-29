class Sorting:
    def __init__(self, array):
        self.array = array
        
    def mergeSort(self):
        self.sort(self.array, [0] * len(self.array), 0, len(self.array)-1)
        print(self.array)

    def sort(self, a, aux, lo, hi):
        if lo < hi:
            mid = (hi+lo) // 2
            self.sort(a, aux, lo, mid)
            self.sort(a, aux, mid+1, hi)
            self.merge(a, aux, lo, mid, hi)

    def merge(self, a, aux, lo, mid, hi):
        for k in range(lo, hi+1):
            aux[k] = a[k]
        i, j = lo, mid+1
        for k in range(lo, hi+1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i+=1
            elif aux[i] <= aux[j]:
                a[k] = aux[i]
                i+=1
            else:
                a[k] = aux[j]
                j+=1



array = [8,9,1,2,3,5,6,0,10,4,6,7]
s = Sorting(array)
s.mergeSort()
