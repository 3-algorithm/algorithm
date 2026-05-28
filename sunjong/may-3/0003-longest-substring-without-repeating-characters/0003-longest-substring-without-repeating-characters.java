class Solution {
    public int lengthOfLongestSubstring(String s) {

        Map<Character, Integer> map = new HashMap<>(); 
        int max = 0;
        
        for (int right = 0, left = 0; right < s.length(); right++) {
            char cur = s.charAt(right);
            if (map.containsKey(cur) && map.get(cur) >= left) { // 없으면 max + 1
                left = map.get(cur) + 1;
            }
            max = Math.max(max, right - left + 1);
            map.put(cur, right);
        }

        return max;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna