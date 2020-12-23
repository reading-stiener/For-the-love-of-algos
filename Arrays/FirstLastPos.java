public class FirstLastPos { 
    public int[] searchRange(int[] nums, int target) {
        int minIdx =  -1;
        int maxIdx =  -1;
        for (int i = 0; i < nums.length; i++) { 
            if (nums[i] == target) { 
                if (minIdx == -1) { 
                    minIdx = i;
                    maxIdx = i;
                } else { 
                    maxIdx = i;
                }
            }
        }
        return new int[] { minIdx, maxIdx };
    }
    public static int binarySearch(int[] nums, int target) { 
        int l = 0;
        int r = nums.length - 1;
        while (l<r) {
            int mid = (l + r) / 2;
            if (mid > target) { 
                r = mid - 1;
            } else if (mid < target) { 
                l = mid + 1;
            } else { 
                return mid; 
            }
        }
        return -1;
    }
    public int [] searchRangeFaster(int[] nums, int target) {
        int minIdx =  -1;
        int maxIdx =  -1;
        int mid = binarySearch(nums, target);
        if (mid == -1) return new int [] {-1, -1};
        else { 
            minIdx = mid;
            while ((minIdx-1)>=0 && nums[minIdx-1]==target) {
                minIdx -= 1;
            }
            maxIdx = mid;
            while ((maxIdx+1)<nums.length && nums[maxIdx+1]==target) {
                maxIdx += 1;
            }
            System.out.println(maxIdx);
            return new int[] {minIdx, maxIdx};
        }
    }
    public static void main(String[] args) { 
        FirstLastPos search = new FirstLastPos();
        System.out.println(search.searchRangeFaster(new int[]{1,2,3,4,4,6,7,9,9,9}, 4));

    }
}