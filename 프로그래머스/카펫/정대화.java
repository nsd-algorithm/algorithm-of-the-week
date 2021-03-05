package 프로그래머스.카펫;

class Solution {
    public int[] solution(int brown, int yellow) {
        int y = 3;
        int sumXY = (brown + 4) / 2;

        while ((sumXY - y) * y != brown + yellow) {
            y++;
        }

        return new int[]{sumXY - y, y};
    }
}
