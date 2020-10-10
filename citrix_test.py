## Lets go! Putting my defs below..
def updateTimes(signalOne, signalTwo):
    # Write your code here
    n = len(signalOne)
    m = len(signalTwo)
    sig_len = min(n, m)
    max_signal = -1
    updated = 0
    for i in range(sig_len):
        if signalOne[i] == signalTwo[i] and signalOne[i] > max_signal:
            max_signal = signalOne[i]
            updated += 1
    return updated

def firstOccurrence(s, x):
    # Write your code here
    m = len(x)
    n = len(s)
    dp_table = [[1 if (s[j] == x[i] or s[j] == "*" or x[i] == "*") else 0 for j in range(n)] for i in range(m)]
    
    # traversing through the dp table and finding matches
    for i in range(n):
        if x[0] == s[i]:
            print("matched ", i)
            # try matching rest of x
            idx_s = i
            for j in range(1, m):
                if idx_s + 1 < n: 
                    if dp_table[j][idx_s+1] == 0:
                        break
                    else:
                        print("matching")
                        print(idx_s-i+2, m)
                        if idx_s-i+2 == m:
                            return i
                        idx_s += 1
                else:
                    break
    return -1
 
def countSentences(wordSet, sentences):
    # Write your code here
    anagram_count = {}
    for word in wordSet: 
        word_sorted = "".join(sorted(list(word)))
        print(word_sorted)
        if anagram_count.get(word_sorted, -1) == -1:
            anagram_count[word_sorted] = 1
        else:
            anagram_count[word_sorted] += 1
    print(anagram_count)
    total_sentences = [] 
    for sentence in sentences:
        sentence_perm = 1
        sent = sentence.split()
        for word in sent:
            word_sorted = "".join(sorted(list(word)))
            sentence_perm *= anagram_count[word_sorted]
        total_sentences.append(sentence_perm) 
    return total_sentences
                    

if __name__ == "__main__": 
    # tests
    print("Check")
    print(firstOccurrence("juliasamanthantjulia", "ant"))