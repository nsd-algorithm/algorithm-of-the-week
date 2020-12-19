package 프로그래머스.위장;

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothesMap = new HashMap<>();

        for (String[] cloth : clothes) {
            clothesMap.put(cloth[1], clothesMap.getOrDefault(cloth[1], 0) + 1);
        }

        int answer = 1;

        for (Map.Entry<String, Integer> entry : clothesMap.entrySet()) {
            answer *= (entry.getValue() + 1);
        }


        return answer - 1;
    }
}
