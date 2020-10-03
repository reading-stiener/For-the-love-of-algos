class Solution:
    # my solution.. too memory intensive
    def letterCombinations(self, digits):
        def let_comb(digits):
            num_dict = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
            }
            letter_comb = []
            return let_comb_help(digits, 0, num_dict, letter_comb)
        def let_comb_help(digits, idx, num_dict, arr):
            if idx == len(digits)-1:
                for letter in num_dict[digits[idx]]: 
                    arr.append(letter)
                return arr
            else:
                arr_copy = let_comb_help(digits, idx+1, num_dict, arr[:])
                for letter in num_dict[digits[idx]]: 
                    print(letter)
                    for i in range(len(arr_copy)): 
                        arr.append(letter + arr_copy[i])
                return arr
        return let_comb(digits)

    # leetcode solution. space optimized
    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output

if __name__ == "__main__": 
    s = Solution()
    print(s.letterCombinations1("233243247987879887989"))
