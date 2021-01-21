def solve(k, numbers):
    n = len(numbers)
    if n % k != 0:
        return "No"
    else:
        parts = [[] for i in range(n//k)]

def palindrome(s):
    # Write your code here
    n = len(s)
    count = 0
    for i in range(1,n):
        for j in range(n - i):
            if isPalin(s[j:j+1]):
                count += 1
    return count

def isPalin(s): 
    if len(s) <= 1:
        return True
    elif len(s) == 2:
        return s[0] == s[1]
    else:
        if s[0] == s[-1]:
            return isPalin(s[1:-1])
        else:
            return False

if __name__ == "__main__":
    print(isPalin("aabaaa"))
            
