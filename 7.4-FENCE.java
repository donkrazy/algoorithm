import java.util.Arrays;
import java.util.Scanner;
import java.lang.Math;

public class Fence {
	private static int findMaxArea(String[] line) {
		int[] heights = Arrays.stream(line).mapToInt(Integer::parseInt).toArray();
		int highest = Arrays.stream(heights).max().getAsInt();
		int maxArea = 0;
		for (int h = highest; h > 0; h--) {
			int area = getAreaUnder(heights, h);
			maxArea = Math.max(maxArea, area);
		}
		return maxArea;
	}

	private static int getAreaUnder(int[] heights, int givenHeight) {
		int count = 0;
		int maxWidth = 0;
		for (int h : heights) {
			if (h >= givenHeight) {
				count++;
			} else {
				maxWidth = Math.max(maxWidth, count);
				count = 0;
			}
		}
		return maxWidth * givenHeight;
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num_prob = Integer.parseInt(scanner.nextLine());
		while (num_prob-- > 0) {
			int n = Integer.parseInt(scanner.nextLine());
			String[] line = scanner.nextLine().split(" ");
			System.out.println(findMaxArea(line));
		}
		scanner.close();
	}
}
