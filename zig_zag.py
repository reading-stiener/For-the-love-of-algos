class Solution:
    def convert(self, s, numRows):
        n = len(s)
        row_list = [[] for i in range(numRows)]
        row_count = 0
        idx = 0
        up = True
        while idx < n:
            print(row_count)
            row_list[row_count].append(s[idx])
            idx += 1

            if up:
                if row_count + 1 < numRows:
                    row_count += 1
                else: 
                    up = False
                    row_count -= 1
            else: 
                if row_count - 1  >= 0: 
                    row_count -= 1
                else: 
                    up = True
                    row_count += 1
        convert_str = ''
        print(row_list)
        for row_str_list in row_list: 
            convert_str += ''.join(row_str_list)
        return convert_str

if __name__ == "__main__": 
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))
    print(s.convert('PAYPALISHIRING', 4))
