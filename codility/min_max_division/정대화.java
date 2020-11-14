package codility.min_max_division;

public class Main {

    public static void main(String[] args) {
        int result = new Solution().solution(3, 5, new int[]{2, 1, 5, 1, 2, 2, 2});
        System.out.println(result);
    }


}

class Solution {
    public int solution(int K, int M, int[] A) {
        int min = 0;
        int max = 0;
        int answer = Integer.MAX_VALUE;

        for (int a : A) {
            max += a;
        }

        while (min <= max) {
            int mid = (min + max) / 2;

            int cnt = 0;
            int index = 0;
            int cur = 0;
            while (cnt < K && index < A.length) {
                cur += A[index];

                if (cur <= mid) {
                    index++;
                } else {
                    cnt++;
                    cur = 0;
                }
            }

            if (index < A.length) {
                min = mid + 1;
            } else if (cnt <= K) {
                if (mid < answer) {
                    answer = mid;
                }

                max = mid - 1;
            }
        }

        return answer;
    }
}
