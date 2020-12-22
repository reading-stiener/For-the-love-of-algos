class ReverseInteger {
    public int reverse(int x) {
        long rev = 0; 
        boolean neg = (x < 0);
        x = (x < 0) ? x*-1 : x; 
        while(x > 0) { 
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        if (rev > Integer.MAX_VALUE) { 
            return 0;
        } else { 
            if (neg) { 
                return -1 * (int)rev;
            } else { 
                return (int)rev;
            }
        }
    }
        
    public static void main(String[] args) { 
        ReverseInteger s = new ReverseInteger();
        System.out.println(s.reverse(-1213));
    }
}