import math
class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        letter_dict = {}
        n = len(s)
        for i in range(n): 
            if letter_dict.get(s[i], -1) == -1: 
                letter_dict[s[i]] = [i]
            else:
                if len(letter_dict[s[i]]) == 1:
                    letter_dict[s[i]].append(i)
                else: 
                    letter_dict[s[i]][1] = i
        max_len = 0
        for letter, values in letter_dict.items():
            if len(values) > 1:
                max_len = max(max_len, values[1] - values[0])
        return max_len - 1

    def bestTeamScore(self, scores, ages):
        sage_list = []
        n = len(ages)
        for i in range(n): 
            sage_list.append((ages[i], scores[i]))
        sage_list.sort(key=lambda x : x[0])
        max_score = 0
        for i in range(n):
            score = sage_list[i][1]
            high_score = score
            for j in range(i+1,n):
                if sage_list[i][1] <= sage_list[j][1] and high_score <= sage_list[j][1]:
                    score += sage_list[j][1]
                    high_score = sage_list[j][1]
            max_score = max(max_score, score)
        return max_score 

    def findLexSmallestString(self, s, a, b):
        def rot_str(s, b):
            n = len(s)
            rot_list = [[] for i in range(n)]
            for i in range(n):
                rot_list[(i+b)%n] = s[i]
            print("r ",rot_list)
            return "".join(rot_list)
        def add_str(s, a):
            n = len(s)
            add_list = [[] for i in range(n)]
            for i in range(n): 
                if i % 2 == 1:
                    add_list[i] =  str((int(s[i])+a)%10) 
                else: 
                    add_list[i] = s[i]
            print("a ", add_list)
            return "".join(add_list)
        seen = set()
        queue = [s]
        min_str = s
        while len(queue) > 0:
            print(seen, min_str)
            curr_str = queue.pop(0)
            seen.add(curr_str)
            min_str = min(min_str, curr_str)
            rot_s, add_s = rot_str(curr_str, b), add_str(curr_str, a)
            if rot_s not in seen:
                queue.append(rot_s)
            if add_s not in seen:
                queue.append(add_s)
        return min_str
      

if __name__ == "__main__": 
    s = Solution()
    #print(s.maxLengthBetweenEqualCharacters("ccsfadsfs"))
    print(s.findLexSmallestString("43987654",7, 3))
    #print(s.bestTeamScore([1,2,1,1],[8,9,10,1]))
