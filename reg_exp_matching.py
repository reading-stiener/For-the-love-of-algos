class Solution:
    # recursive solution
    def isMatch(self, s, p):
        if not s:
            return not p
        first_match = bool(s) and (p[0] == s[0] or p[0] == ".")
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])