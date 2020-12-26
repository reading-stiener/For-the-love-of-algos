import java.util.*;
class MultiplyStrings {
    // doesn't work with large inputs
    public String multiply(String num1, String num2) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>(); 
        map.put('0', 0);
        map.put('1', 1);
        map.put('2', 2);
        map.put('3', 3);
        map.put('4', 4);
        map.put('5', 5);
        map.put('6', 6);
        map.put('7', 7);
        map.put('8', 8);
        map.put('9', 9);
        HashMap<Integer, Character> map1 = new HashMap<Integer, Character>(); 
        map1.put(0, '0');
        map1.put(1, '1');
        map1.put(2, '2');
        map1.put(3, '3');
        map1.put(4, '4');
        map1.put(5, '5');
        map1.put(6, '6');
        map1.put(7, '7');
        map1.put(8, '8');
        map1.put(9, '9');
        long numInt1 = this.stringToInt(num1, map);
        long numInt2 = this.stringToInt(num2, map);
        //System.out.println(numInt1);
        //System.out.println(numInt2);
        long mul =  numInt1 * numInt2;
        //System.out.println(mul);
        return this.numToString(mul, map1);
    }
    public long stringToInt(String num, HashMap<Character, Integer> map) { 
        long stringNum = 0;
        for (int i = 0; i < num.length(); i++) { 
            //System.out.println(num.charAt(num.length()-i-1));
            stringNum += map.get(num.charAt(num.length()-i-1)) * Math.pow(10, i);
            //System.out.println(stringNum);
            //System.out.println(num.charAt(num.length()-i-1));
        }
        return stringNum;
    }
    public String numToString(long num, HashMap<Integer, Character> map) {
        StringBuilder stringNum = new StringBuilder();
        if (num == 0) { 
            return "0";
        }
        while (num > 0) { 
            //System.out.println(num%10);
            stringNum.append(map.get((int)(num%10)));
            num /= 10; 
        }
        return stringNum.reverse().toString();
    }
    public String multiplyBetter(String num1, String num2) { 
        if (num1.equals("0") || num2.equals("0")) { 
            return "0";
        }
        int[] mul = new int[401]; 
        int start = 400;
        StringBuilder mulStr = new StringBuilder();
        int idx = start;
        for (int i = num1.length()-1; i >= 0; i--) { 
            int carry = 0;
            idx = start;
            for (int j = num2.length()-1; j >= 0; j--) { 
                int val = (num1.charAt(i) - '0') * (num2.charAt(j) - '0') + mul[idx] + carry;
                mul[idx] = val % 10;
                carry = val / 10;
                idx--;
            }
            while (carry > 0) { 
                //System.out.println("array val " + Integer.toString(mul[idx]));
                mul[idx] = (carry + mul[idx]) % 10;
                carry = mul[idx] / 10; 
                idx--;
            }
            start--; 
        }
        for (int i = idx+1; i <= 400; i++) { 
            mulStr.append(Integer.toString(mul[i]));
        }
        //System.out.println(Arrays.toString(mul));
        return mulStr.toString();
    }   

    public static void main(String[] args) { 
        MultiplyStrings s = new MultiplyStrings();
        System.out.println(s.multiplyBetter("9301", "0"));
        //System.out.println(10.1/10);
    }
}