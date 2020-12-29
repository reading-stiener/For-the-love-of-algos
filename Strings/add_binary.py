class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n_a = len(a)
        n_b = len(b)
        carry = '0'
        copy_a = a[::-1]
        copy_b = b[::-1]
        add_str = ''
        for i in range(max(n_a, n_b)): 
            if i >= len(a):
                if carry == '1' and copy_b[i] == '1':
                    add_str += 0
                    carry = '1'
                elif carry == '1' and copy_b[i] == '0': 
                    add_str += '1' 
                    carry = '0'
                elif carry == '0' and copy_b[i] == '1': 
                    add_str += '1'
                    carry = '0'
                else: 
                    add_str += '0'
                    carry = '0'
            elif i >= len(b):
                if carry == '1' and copy_a[i] == '1':
                    add_str += '0'
                    carry = '1'
                elif carry == '1' and copy_a[i] == '0':
                    add_str += '1' 
                    carry = '0'
                elif carry == '0' and copy_a[i] == '1': 
                    add_str += '1'
                    carry = '0'
                else: 
                    add_str += '0'
                    carry = '0'
            else:
                if carry == '0' and copy_a[i] == '0' and copy_b[i] == '0':
                    add_str += '0'
                    carry = '0'
                elif carry == '0' and copy_a[i] == '0' and copy_b[i] == '1':
                    add_str += '1'
                    carry = '0'
                elif carry == '0' and copy_a[i] == '1' and copy_b[i] == '0':
                    add_str += '1'
                    carry = '0'
                elif carry == '0' and copy_a[i] == '1' and copy_b[i] == '1':
                    add_str += '1'
                    carry = '1'
                elif carry == '1' and copy_a[i] == '0' and copy_b[i] == '0':
                    add_str += '1'
                    carry = '0'
                elif carry == '1' and copy_a[i] == '0' and copy_b[i] == '1':
                    add_str += '0'
                    carry = '1'
                elif carry == '1' and copy_a[i] == '1' and copy_b[i] == '0':
                    add_str += '0'
                    carry = '1'
                elif carry == '1' and copy_a[i] == '1' and copy_b[i] == '1':
                    add_str += '1'
                    carry = '1'
        if carry == '1':
            add_str += '1'

        return add_str

    # bitwise solution 
    def addBinaryBit(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return "{0:b}".format(x)

if __name__ == "__main__":
    s = Solution()
    print(s.addBinaryBit('1111', '0010'))