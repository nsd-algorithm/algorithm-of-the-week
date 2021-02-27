package 프로그래머스.다리를_지나는_트럭;

import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;

        int[] times = new int[truck_weights.length];
        Arrays.fill(times, bridge_length);
        Queue<Integer> truckQueue = new ArrayDeque<>();

        for (int i = 0; i < truck_weights.length; ) {
            moveTruck(times, truckQueue);

            answer++;

            int currentTotalWeight = truckQueue.stream()
                    .mapToInt(index -> truck_weights[index])
                    .sum() + truck_weights[i];

            if (currentTotalWeight <= weight) {
                truckQueue.add(i);
                i++;
            }
        }

        while (!truckQueue.isEmpty()) {
            moveTruck(times, truckQueue);

            answer++;
        }

        return answer;
    }

    private void moveTruck(int[] times, Queue<Integer> truckQueue) {
        for (int truck : truckQueue) {
            times[truck]--;
        }

        while (!truckQueue.isEmpty() && times[truckQueue.peek()] == 0) {
            truckQueue.poll();
        }
    }
}
