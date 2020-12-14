class Solution:
    def mergeSort(self, arr):
        if len(arr) >1:
            mid = len(arr)//2 # Finding the mid of the array
            L = arr[:mid] # Dividing the array elements
            R = arr[mid:] # into 2 halves

            self.mergeSort(L) # Sorting the first half
            self.mergeSort(R) # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i+= 1
                else:
                    arr[k] = R[j]
                    j+= 1
                k+= 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i+= 1
                k+= 1

            while j < len(R):
                arr[k] = R[j]
                j+= 1
                k+= 1


if __name__ == '__main__':
    input = [2, 8, 4, 5, 7, 1]
    solution = Solution()
    solution.mergeSort(input)
    print(input)