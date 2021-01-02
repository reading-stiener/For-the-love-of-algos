class PalindromeNum {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        return palindrome(s);

    }
    static boolean palindrome(String x) {
        System.out.println(x);
        if (x.length() == 1) { 
            return true;
        } else if (x.length() == 2) { 
            return x.charAt(0) == x.charAt(1);
        } else { 
            if (x.charAt(0) == x.charAt(x.length()-1)) { 
                return palindrome(x.substring(1, x.length()-1));
            }
            else return false;
        }
    }
    public static void main(String[] args){ 
        PalindromeNum sol = new PalindromeNum();
        System.out.println(sol.isPalindrome(121));
    }
}