package 백준.p11404

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int MAX = 100 * 100_000 + 1;

        int[][] cites = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cites[i][j] = i != j ? MAX : 0;
            }
        }

        for (int i = 0; i < m; i++) {
            int[] busInfo = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            if (busInfo[2] < cites[busInfo[0] - 1][busInfo[1] - 1]) {
                cites[busInfo[0] - 1][busInfo[1] - 1] = busInfo[2];
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (cites[i][k] + cites[k][j] < cites[i][j]) {
                        cites[i][j] = cites[i][k] + cites[k][j];
                    }
                }
            }
        }

        String result = Arrays.stream(cites)
                .parallel()
                .map(Arrays::stream)
                .map(intStream -> intStream.map(i -> i == MAX ? 0 : i))
                .map(intStream -> intStream.mapToObj(String::valueOf))
                .map(stringStream -> stringStream.collect(Collectors.joining(" ")))
                .collect(Collectors.joining(System.lineSeparator()));

        System.out.println(result);
    }
}
