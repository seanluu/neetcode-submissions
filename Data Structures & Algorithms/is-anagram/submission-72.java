class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> anagramS = new HashMap<>();
        HashMap<Character, Integer> anagramT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            anagramS.put(s.charAt(i), anagramS.getOrDefault(s.charAt(i), 0) + 1);
            anagramT.put(t.charAt(i), anagramT.getOrDefault(t.charAt(i), 0) + 1);
        }

        return anagramS.equals(anagramT);

    }
}
