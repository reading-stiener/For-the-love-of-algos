class Solution:

    def topKFrequent(self, nums, k):
        n = len(nums)
        def mergearrays(start, end, arr, mid):
            
            arr_left = arr[start:mid+1]
            arr_right = arr[mid+1:end+1]
            print("left ", arr_left)
            print("right ", arr_right)
            l_l, l_r = len(arr_left), len(arr_right) 
            idx_l, idx_r = 0, 0
            idx = start
            while idx_l < l_l or idx_r < l_r:
                if idx_l == l_l:
                    arr[idx] = arr_right[idx_r]
                    idx_r += 1
                    idx += 1
                elif idx_r == l_r:
                    arr[idx] = arr_left[idx_l]
                    idx_l += 1
                    idx += 1
                else:
                    if arr_left[idx_l] < arr_right[idx_r]:
                        arr[idx] = arr_left[idx_l]
                        idx_l += 1
                        idx += 1
                    else:
                        arr[idx] = arr_right[idx_r]
                        idx_r += 1
                        idx += 1
            return arr
        def mergesort(arr, start, end):
            print("full arr ", arr)
            if start < end:
                print(start, end)
                mid = (start + end) // 2
                mergesort(arr, start, mid)
                mergesort(arr, mid+1, end)
                mergearrays(start, end, arr, mid)
                return arr
        sorted_nums = mergesort(nums, 0, n-1)
        print(sorted_nums)

if __name__ == "__main__": 
    s = Solution()
    s.topKFrequent([5,23,6,2,0,6,231],2)