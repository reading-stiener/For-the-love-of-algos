class Solution:
    def __init__(self):
        self.abbr = []

    # backtracking
    def generateAbbreviations(self, word):
        n = len(word)
        alpha = "abcdefghijklmnopqrstuvwxyz"
        abbr_list = []
        def gen_abbr(abbr, word, idx, n, count):
            if idx == n:
                #self.abbr.append(abbr)
                abbr_list.append(abbr)
            else:
                if abbr and abbr[-1] not in alpha:
                    gen_abbr(abbr[:-1]+str(count+1), word, idx+1, n, count+1)
                else: 
                    gen_abbr(abbr+str(count+1), word, idx+1, n, count+1)
                gen_abbr(abbr+word[idx], word, idx+1, n, 0)

        gen_abbr("", word, 0, n, 0)
        #return self.abbr
        return abbr_list

    ## bitwise solution    
    def abbr_bit(self, word, x):
        k = 0
        n = len(word)
        abbr = ""
        for i in range(n):
            if x & 1 == 1: 
                k += 1
            else:
                if k != 0:
                    abbr += str(k)
                    k = 0
                abbr +=  word[i]
            x >>= 1
        if k != 0:
            abbr += str(k)
        return abbr
    
    def bit_wise(self, word):
        n = len(word)
        abbr = []
        for i in range(1 << n):
            abbr.append(self.abbr_bit(word, i))
        return abbr


if __name__ == "__main__":
    s = Solution()
    print(s.generateAbbreviations("three"))
    print(s.bit_wise("three"))
    #print(s.abbr_bit("two", 4))
