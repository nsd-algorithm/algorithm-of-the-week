package 백준.p13417;

import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            char[] cards = br.readLine()
                    .replaceAll(" ", "")
                    .toCharArray();

            System.out.println(getResult(cards));
        }
    }

    public static String getResult(char[] cards) {
        Deque<Character> result = new ArrayDeque<>();

        for (char card : cards) {
            char firstChar = result.peekFirst() != null ? result.peekFirst() : 0;

            if (firstChar < card) {
                result.offerLast(card);
            } else if (card <= firstChar) {
                result.offerFirst(card);
            }
        }

        StringBuilder sb = new StringBuilder();

        for (char c : result) {
            sb.append(c);
        }

        return sb.toString();
    }
}
