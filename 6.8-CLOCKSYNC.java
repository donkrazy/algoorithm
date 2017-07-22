import java.util.Arrays;
import java.util.Scanner;


public class Clocksync {
    static int INF = 99999;
    static int NUM_SWITCHES = 10;
    static int[][] switchInfo = {
            {0, 1, 2},              // SWITCH 0
            {3, 7, 9, 11},          // SWITCH 1
            {4, 10, 14, 15},        // SWITCH 2
            {0, 4, 5, 6, 7},        // SWITCH 3
            {6, 7, 8, 10, 12},      // SWITCH 4
            {0, 2, 14, 15},         // SWITCH 5
            {3, 14, 15},            // SWITCH 6
            {4, 5, 7, 14, 15},      // SWITCH 7
            {1, 2, 3, 4, 5},        // SWITCH 8
            {3, 4, 5, 9, 13}        // SWITCH 9
    };

    static boolean areAligned(int[] clocks) {
        for (int time : clocks) {
            if (time != 12) {
                return false;
            }
        }
        return true;
    }

    static void pushSwitch(int[] clocks, int switchIdx) {
        for (int clockIdx : switchInfo[switchIdx]) {
            clocks[clockIdx] += 3;
            if (clocks[clockIdx] == 15) {
                clocks[clockIdx] = 3;
            }
        }
    }

    static int solve(int[] clocks, int switchIdx) {
        if (switchIdx == NUM_SWITCHES) {
            return areAligned(clocks) ? 0 : INF;
        }
        int ret = INF;
        for (int count = 0; count < 4; count++) {
            ret = Math.min(ret, count + solve(clocks, switchIdx + 1));
            pushSwitch(clocks, switchIdx);
        }
        return ret;
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num_prob = Integer.parseInt(scanner.nextLine());
        while (num_prob-- > 0) {
            String[] line = scanner.nextLine().split(" ");
            int[] clocks = Arrays.stream(line).mapToInt(Integer::parseInt).toArray();
            int ret = solve(clocks, 0);
            System.out.println(ret < INF ? ret : -1);
        }
        scanner.close();
    }
}
