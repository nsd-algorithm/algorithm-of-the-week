package 프로그래머스.징검다리;

import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int[] distances = new int[rocks.length + 1];

        // 정렬 후 각 칸의 사이 거리 저장
        Arrays.sort(rocks);

        distances[0] = rocks[0];
        distances[distances.length - 1] = distance - rocks[rocks.length - 1];

        for (int i = 1; i < rocks.length; i++) {
            distances[i] = rocks[i] - rocks[i - 1];
        }
        // 투포인터
        int maxDistance = distance;
        int minDistance = 0;
        int result = 0;

        while (minDistance <= maxDistance) {
            int curDistance = (maxDistance + minDistance) / 2;
            int[] distancesCopy = distances.clone();
            int removeCount = 0;

            for (int i = 0; i < distancesCopy.length - 1; i++) {
                if (distancesCopy[i] < curDistance) {
                    distancesCopy[i + 1] += distancesCopy[i];

                    if(n < ++removeCount) {
                        break;
                    }
                }
            }

            if (removeCount <= n) {
                minDistance = curDistance + 1;
                if(result < curDistance) {
                    result = curDistance;
                }

            } else {
                maxDistance = curDistance - 1;
            }
        }

        return result;
    }
}
