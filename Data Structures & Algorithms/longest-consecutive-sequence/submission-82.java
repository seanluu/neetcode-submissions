class Solution {
    public int longestConsecutive(int[] nums) {

        int res = 0;

        Set<Integer> numSet = new HashSet<>();

        for (int num : nums) {
            numSet.add(num);
        }

        for (int num : numSet) {
            if (!numSet.contains(num - 1)) {
                int length = 1;
                while (numSet.contains(num + length)) {
                    length++;
                }
                res = Math.max(length, res);
            }
        }
        return res;
    }
}
