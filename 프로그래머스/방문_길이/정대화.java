package 프로그래머스.방문_길이;

import java.util.*;

class Solution {
    public int solution(String dirs) {
        Set<Edge> edges = new HashSet<>();

        Point cur = new Point(0, 0);
        Point prev = new Point(0, 0);

        for (String dir : dirs.split("")) {
            Point temp = prev;
            switch (dir) {
                case "U": {
                    prev = cur;
                    cur = new Point(cur.x, cur.y + 1);
                    break;
                }
                case "D": {
                    prev = cur;
                    cur = new Point(cur.x, cur.y - 1);
                    break;
                }
                case "R": {
                    prev = cur;
                    cur = new Point(cur.x + 1, cur.y);
                    break;
                }
                case "L": {
                    prev = cur;
                    cur = new Point(cur.x - 1, cur.y);
                    break;
                }
            }

            if (-5 <= cur.x && -5 <= cur.y && cur.x <= 5 && cur.y <= 5) {
                edges.add(new Edge(prev, cur));
            } else {
                cur = prev;
                prev = temp;
            }
        }

        return edges.size();
    }

    private static class Edge {
        Point a;
        Point b;

        public Edge(Point a, Point b) {
            // Point[] points = new Point[]{a, b};

            // Arrays.sort(points);

            this.a = a;
            this.b = b;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Edge edge = (Edge) o;
            return Objects.equals(a, edge.a) && Objects.equals(b, edge.b);
        }

        @Override
        public int hashCode() {
            return Objects.hash(a, b) + Objects.hash(b, a);
        }
    }

    private static class Point implements Comparable<Point> {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Point point = (Point) o;
            return x == point.x && y == point.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public int compareTo(Point o) {
            int result = Integer.compare(x, o.x);

            if (result == 0) {
                result = Integer.compare(y, o.y);
            }

            return result;
        }
    }
}
