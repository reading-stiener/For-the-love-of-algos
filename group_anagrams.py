class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = {}
        for word in strs:
            letterlist = sorted(list(word))
            word_sorted = "".join(letterlist)
            if anagram_dict.get(word_sorted, -1) == -1:
                anagram_dict[word_sorted] = [word]
            else:
                anagram_dict[word_sorted] += [word]
        anagrams = []
        for group, agrams in anagram_dict.items():
            anagrams.append(agrams)
        return anagrams

    def gen_anagrams(self, word):
        anagram_list = []
        def anagrams(word, a_gram):
            if len(word) == 1:
                anagram_list.append(a_gram + word[0])
            for i in range(len(word)):
                anagrams(word[:i] + word[i+1:], a_gram+word[i])
        anagrams(word,"")
        return anagram_list

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["hello", "tea", "eat"]))         
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(s.gen_anagrams("hello"))