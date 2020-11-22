class Solution:
    def validIPAddress(self, IP):
        def ipv6_patt(unit):
            pat = "abcdef0123456789"
            for char in unit:
                if char not in pat:
                    print(char)
                    return False
            return True
        IP = IP.lower()
        print(IP)
        if "." in IP: # ipv4 address 
            addr_list = IP.split(".")
            if len(addr_list) != 4:
                return "Neither"
            for unit in addr_list: 
                try:
                    if int(unit) >= 0 and int(unit)<= 255 and unit == str(int(unit)): 
                        pass
                    else:
                        return "Neither"
                except:
                    return "Neither"
            return "IPv4"
        elif ":" in IP: # ipv6 address
            addr_list = IP.split(":")
            if len(addr_list) != 8:
                return "Neither"
            for unit in addr_list:
                if len(unit) > 4 or not ipv6_patt(unit): 
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"
if __name__ == "__main__":
    s = Solution()
    print(s.validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))
