import java.util.*;
class MultiplyStrings {
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
    public static void main(String[] args) { 
        MultiplyStrings s = new MultiplyStrings();
        System.out.println(s.multiply("6913259244", "71103343"));
    }
}