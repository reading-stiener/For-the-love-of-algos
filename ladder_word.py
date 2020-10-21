import math
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        def diff_check(word1, word2):
            diff_count = 0
            n = len(word1)
            for i in range(n):
                if word1[i] != word2[i]:
                    diff_count += 1
                if diff_count > 1:
                    return -1
            if diff_count == 1:
                return 0
            else:
                return 1
        min_steps = math.inf
            #print(min_steps)
        def brute_force_check(curr_word, endWord, wordList, steps, min_steps):
            n = len(wordList)
            for i in range(n):
                if diff_check(curr_word, endWord) == 1:
                    min_steps = min(min_steps, steps)
                elif diff_check(curr_word, wordList[i]) == 0:
                    wordList_c = wordList[:i] + wordList[i+1:]
                    min_steps = brute_force_check(wordList[i], endWord, wordList_c, steps+1, min_steps)
            return min_steps
        ans = brute_force_check(beginWord, endWord, wordList, 1, min_steps)
        if ans == math.inf:
            return 0
        else: 
            return ans

if __name__  == "__main__": 
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
        
