class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for email in emails: 
            email_split = email.split("@")
            print(email_split)
            local = email_split[0].replace(".", "")
            idx = local.find("+")
            if idx != -1:
                local = local[:idx]
            if local+"@"+email_split[1] not in unique_emails:
                unique_emails.add(local+"@"+email_split[1])
        return len(unique_emails)

if __name__ == "__main__": 
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))