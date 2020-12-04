import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        Integer[] network = new Integer[n];
        Arrays.fill(network, 0);

        for(int i = 0; i < computers.length; i++) {
            Stack<int[]> stack = new Stack<>();

            if(network[i] == 0) {
                network[i] = i + 1;
                stack.push(computers[i]);
            }

            while(!stack.isEmpty()) {
                int[] currents = stack.pop();

                for(int j = 0; j < currents.length; j++) {
                    if(currents[j] == 1 && network[j] == 0) {
                        network[j] = i + 1;
                        stack.push(computers[j]);
                    }
                }
            }
        }

        Set<Integer> set = new HashSet(Arrays.asList(network));


        return set.size();
    }
}
