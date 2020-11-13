package prgrms.기능개발;

import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<Result> inputs = Arrays.asList(
                new Main().new Result(
                        0,
                        new int[]{93, 30, 55},
                        new int[]{1, 30, 5}
                ), new Main().new Result(
                        1,
                        new int[]{95, 90, 99, 99, 80, 99},
                        new int[]{1, 1, 1, 1, 1, 1}
                )
        );

        for (Result input : inputs) {
            printResult(input.index, input.progresses, input.speeds);
        }
    }

    private static void printResult(int index, int[] progresses, int[] speeds) {
        System.out.println(index + " : " + Arrays.toString(new Solution().solution(progresses, speeds)));
    }

    class Result {
        int index;
        int[] progresses;
        int[] speeds;

        public Result(int index, int[] progresses, int[] speeds) {
            this.index = index;
            this.progresses = progresses;
            this.speeds = speeds;
        }
    }
}

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();

        ListIterator<Integer> progressesIter = Arrays.stream(progresses)
                .boxed()
                .collect(Collectors.toList())
                .listIterator();

        int time = 0;

        while (progressesIter.hasNext()) {
            int buildCount = 1;
            int currentIndex = progressesIter.nextIndex();
            int currentProgress = progressesIter.next();

            while (currentProgress + time * speeds[currentIndex] < 100) {
                time++;
            }

            while (progressesIter.hasNext() &&
                    100 <= progresses[progressesIter.nextIndex()] + time * speeds[progressesIter.nextIndex()]) {
                buildCount++;
                progressesIter.next();
            }

            answer.add(buildCount);
        }
        return answer.stream()
                .mapToInt(Integer::valueOf)
                .toArray();
    }
}
