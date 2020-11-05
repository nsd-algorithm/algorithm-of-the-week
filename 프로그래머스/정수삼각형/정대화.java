package 프로그래머스.정수삼각형;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        
        for (int i = triangle.length - 2; 0 <= i; i--) {
            for (int j = 0; j < triangle[i].length; j++) {
                triangle[i][j] += Math.max(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        
        return triangle[0][0];
    }
}
