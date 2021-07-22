package 프로그래머스.멀쩡한_사각형;

import java.math.BigInteger;

class Solution {
    public long solution(int w, int h) {
        BigInteger width = BigInteger.valueOf(w);
        BigInteger height = BigInteger.valueOf(h);

        BigInteger gcd = width.gcd(height);

        long numberOfCanNotUse = width.add(height)
                                         .subtract(gcd)
                                         .longValue();

        long answer = width.multiply(height).longValue() - numberOfCanNotUse;

        return answer;
    }
}
