from collections import Counter
class Solution:
    def frequencySort(self, s):
        char_dict = Counter()
        for char in s:
            char_dict[char] += 1
        char_list = [(val, char) for char, val in char_dict.items()]
        char_list.sort(key=lambda x : x[0], reverse=True)
        ans = ""
        for char_tup in char_list:
            ans += char_tup[1] * char_tup[0]
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("tree"))
