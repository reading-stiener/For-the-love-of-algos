from collections import Counter
class Solution:
    def numUniqueEmails(self, emails):
        unique_emails = set()
        for email in emails:
            # remove dots before domain name
            local, domain = email.split("@")
            local = local.replace(".", "")
            # remove part after first +
            idx = local.find("+")
            if idx != -1:
                unique_emails.add(local[:idx]+"@"+ domain)
        return len(unique_emails)
    
    def totalFruit(self, tree):
        n = len(tree)
        basket = Counter()
        l, r = 0, 0
        max_fruits = 0
        count = 0
        while r < n:
            #print(r, count, basket, len(basket))
            if len(basket) < 2:
                basket[tree[r]] += 1
                count += 1
                r += 1
            elif len(basket) == 2 and basket[tree[r]] > 0:
                basket[tree[r]] += 1
                count += 1
                r += 1
            else: # note the sum and move the counter
                basket[tree[r]] += 1
                count += 1
                r += 1
                while len(basket) > 2:
                    #print("deleted keys {} ".format(l))
                    #print(basket)
                    basket[tree[l]] -= 1
                    count -= 1
                    if basket[tree[l]] == 0:
                        del basket[tree[l]]
                    l += 1
            max_fruits = max(max_fruits, count)
        return max_fruits         

if __name__ == "__main__":
    s = Solution()
    print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))



