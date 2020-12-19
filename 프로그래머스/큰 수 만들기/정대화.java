import java.util.*;

class Solution {
    public String solution(String number, int k) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < number.length(); i++) {
            int cur = charToInt(number.charAt(i));
            for (; 0 < result.length() && charToInt(result.charAt(result.length() - 1)) < cur && 0 < k; k--) {
                result.deleteCharAt(result.length() - 1);
            }
            if (result.length() < number.length() - k) {
                result.append(cur);
            }
        }

        return result.toString();
    }

    public static int charToInt(char c) {
        return Character.digit(c, 10);
    }
}
