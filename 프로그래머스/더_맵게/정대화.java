package 프로그래머스.더_맵게;

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;

        Queue<Integer> scovilleQueue = new PriorityQueue();
        for (int i = 0; i < scoville.length; i++)
            scovilleQueue.add(scoville[i]);

        while (1 < scovilleQueue.size() && scovilleQueue.peek() < K) {
            scovilleQueue.add(scovilleQueue.poll() + scovilleQueue.poll() * 2);
            answer++;
        }

        if (scovilleQueue.poll() < K)
            return -1;

        return answer;
    }
}
