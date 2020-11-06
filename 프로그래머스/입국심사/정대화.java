package 프로그래머스.입국심사;

class Main {
    public static void main(String[] args) {
        int input1_1 = 6;
        int[] input1_2 = new int[]{7, 10};
        int input2_1 = 8;
        int[] input2_2 = new int[]{3, 5, 10};
        int input3_1 = 5;
        int[] input3_2 = new int[]{1, 2, 4};

        printResult(input1_1, input1_2);
        printResult(input2_1, input2_2);
        printResult(input3_1, input3_2);

    }

    public static void printResult(int input_1, int[] input_2) {
        System.out.println(new Solution().solution(input_1, input_2));
    }
}

class Solution {
    public long solution(int n, int[] times) {
        long answer = Long.MAX_VALUE;

        long maxTime = 0;

        for (int time : times) {
            if (maxTime < time) {
                maxTime = time;
            }
        }

        maxTime *= n;

        long minTime = 0;

        while (minTime <= maxTime) {
            long curTime = (minTime + maxTime) / 2;

            long permittedPeople = 0;

            for (int time : times) {
                permittedPeople += curTime / time;
            }

            if (n <= permittedPeople) {
                if (curTime < answer) {
                    answer = curTime;
                    maxTime = curTime - 1;
                }
            } else {
                minTime = curTime + 1;
            }
        }

        return answer;
    }
}
