import math
from collections import defaultdict, deque
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
        adj_dict = defaultdict(lambda : None)
        def make_adj(wordList):
            for wordi in wordList:
                for wordj in wordList:
                    if wordj != wordi and diff_check(wordi, wordj) == 0:
                        if adj_dict[wordi] == None:
                            adj_dict[wordi] = [wordj]
                        else:
                            adj_dict[wordi].append(wordj)
        make_adj(wordList+[beginWord])
        print(adj_dict)
        visited = set()
        queue = deque()
        queue.append((beginWord,1))
        while len(queue) > 0:
            curr = queue.popleft()
            if curr[0] in visited:
                continue
            # print(queue)
            # print(curr)
            visited.add(curr[0])
            if curr[0] == endWord:
                return curr[1]
            for adj in adj_dict[curr[0]]:
                if diff_check(curr[0], adj) == 0 and adj not in visited:
                    queue.append((adj,curr[1]+1))
        return 0

if __name__  == "__main__": 
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
        
