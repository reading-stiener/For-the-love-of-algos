import java.util.*;
class Tree { 
    public int x; 
    public Tree l; 
    public Tree r; 
}
public class HRT { 
    int maxLen = 0;
    Set<Integer> visited = new HashSet<>();
    public int solution(Tree T) {
        // write your code in Java SE 8
        this.dfs(T, this.maxLen, this.visited, 0);
        return maxLen;

    }
    public void dfs(Tree root, int maxLen, Set<Integer> visited, int depth) { 
        if (root != null) { 
            // base case I. Node val already seen
            if (visited.contains(root.x)) { 
                this.maxLen = Math.max(maxLen, depth+1);
            } else if (root.l == null && root.r == null) { 
                this.maxLen = Math.max(maxLen, depth+1);
            } else { 
                visited.add(root.x);
                this.dfs(root.l, maxLen, visited, depth+1);
                this.dfs(root.r, maxLen, visited, depth+1);
            }
        }
    }
    public int solution(String S) {
        // write your code in Java SE 8
        String [] input = S.split(" ");
        // make a stack
        System.out.println(input);
        ArrayDeque<String> stack = new ArrayDeque<>();
        for (int i = 0; i < input.length; i++) { 
            if (this.isNumeric(input[i])) { 
                stack.push(input[i]); 
            } else if (input[i].equals("POP")) { 
                if (!stack.isEmpty()) { 
                    stack.pop();
                } else { 
                    return -1;
                }
            } else if (input[i].equals("DUP")) { 
                if (!stack.isEmpty()) { 
                    stack.push(stack.peek());
                } else { 
                    return -1;
                }
            } else if (input[i].equals("+")) { 
                if (stack.size() >= 2) { 
                    String a = stack.pop();
                    String b = stack.pop();
                    if (this.isNumeric(a) &&  this.isNumeric(b)) { 
                        int ans = Integer.parseInt(a) + Integer.parseInt(b);
                        if (ans > 0 && ans < Math.pow(2, 20)) { 
                            stack.push(Integer.toString(ans));
                        } else {
                            return -1;
                        } 
                    }  else { 
                        return -1; 
                    }
                } else { 
                    return -1;
                }
            } else if (input[i].equals("-")) { 
                if (stack.size() >= 2) { 
                    String a = stack.pop();
                    String b = stack.pop();
                    if (this.isNumeric(a) &&  this.isNumeric(b)) { 
                        int ans = Integer.parseInt(a) - Integer.parseInt(b);
                        if (ans > 0 && ans < Math.pow(2, 20)) { 
                            stack.push(Integer.toString(ans));
                        } else {
                            return -1;
                        } 
                    }  else { 
                        return -1; 
                    }
                } else { 
                    return -1;
                }
            } else { 
                return -1;
            }
        }
        if (!stack.isEmpty()) { 
            return Integer.parseInt(stack.pop());
        } else { 
            return -1;
        }
    }

    public boolean isNumeric(final String str) {

        // null or empty
        if (str == null || str.length() == 0) {
            return false;
        }
        for (char c : str.toCharArray()) {
            if (!Character.isDigit(c)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) { 
        System.out.println("All my tests go below. Lets go!!");
        HRT test = new HRT();
        String input = "4 5 6 7 -";
        test.solution(input);
    }
}