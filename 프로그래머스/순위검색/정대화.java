package prgrms.순위검색;

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];

        Trie trie = new Trie();

        for (String row : info) {
            trie.add(row.split(" "));
        }

        for (int i = 0; i < query.length; i++) {
            String[] rows = Arrays.stream(query[i].split(" "))
                                    .filter(s -> !s.equals("and"))
                                    .collect(Collectors.toList()).toArray(new String[]{});

            answer[i] = trie.count(rows);
        }

        return answer;
    }
}

class Trie {
    private TrieNode root = new TrieNode();

    public void add(String[] row) {
        root.add(row, 0);
    }

    public int count(String[] query) {
        return root.count(query, 0);
    }
}

class TrieNode {
    private Map<String, TrieNode> children = new HashMap<>();
    private List<Integer> scores = new ArrayList<>();
    private boolean isEndedAtNext;
    private int count;

    public void add(String[] row, int index) {
        if (index + 1 < row.length) {
            TrieNode child;

            if (!children.containsKey(row[index])) {
                child = new TrieNode();
                children.put(row[index], child);
            } else {
                child = children.get(row[index]);
            }

            child.add(row, index + 1);
        } else {
            isEndedAtNext = true;
            scores.add(Integer.parseInt(row[row.length - 1]));
            scores.sort(Integer::compareTo);
        }
    }

    public int count(String[] query, int index) {
        if (isEndedAtNext) {
            int min = 0;
            int max = scores.size();

            int target = Integer.parseInt(query[query.length - 1]);

            while (min < max) {
                int mid = (min + max) / 2;

                int cur = scores.get(mid);

                if (cur < target) {
                    min = mid + 1;
                } else {
                    max = mid;
                }
            }

            return scores.size() - max;
        }

        if (query[index].equals("-")) {
            int result = 0;

            for (Map.Entry<String, TrieNode> entry : children.entrySet()) {
                result += entry.getValue().count(query, index + 1);
            }

            return result;
        }

        if (!children.containsKey(query[index])) {
            return 0;
        }

        return children.get(query[index]).count(query, index + 1);
    }
}
