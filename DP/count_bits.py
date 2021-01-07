class Solution:
    def countBits(self, num):
        def pow_two(n):
            #print("n ", n)
            if n == 1:
                return True
            elif n < 1 or n % 2 > 0: 
                return False
            else:
                return pow_two(n/2)
        if num == 0:
            return 0
        elif num == 1: 
            return 1
        count_list = [0, 1]
        i = 2
        track_idx = 0
        while i <= num:
            #print(i, end=" ")
            if pow_two(i):
                #print("is pow of 2")
                track_idx = 0
            count_list.append(1+count_list[track_idx])
            track_idx += 1
            i += 1
        return count_list
            
if __name__ == "__main__":
    s = Solution()
    print(s.countBits(16))
