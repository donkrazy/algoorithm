import java.util.Arrays;
import java.util.Scanner;

public class Fence {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num_prob = Integer.parseInt(scanner.nextLine());
		while (num_prob-- > 0) {
			int n = Integer.parseInt(scanner.nextLine());
			String[] line = scanner.nextLine().split(" ");
			int[] heights = Arrays.stream(line).mapToInt(Integer::parseInt).toArray();
			System.out.println(findMaxArea(heights, 0, n - 1));
		}
		scanner.close();
	}

	private static int findMaxArea(int[] heights, int left, int right) {
		// 1) base case
		if (left == right) {
			return heights[left];
		}

		// 2) left or right max case
		int mid = (left + right) / 2;
		int leftMax = findMaxArea(heights, left, mid);
		int rightMax = findMaxArea(heights, mid + 1, right);
		int ret = Math.max(leftMax, rightMax);

		// 3) center overlapping case
		// start point: rectangle with (mid, 0), (mid+1, heights[mid+1])
		int i = mid;
		int j = mid + 1;
		int h = Math.min(heights[i], heights[j]);
		ret = Math.max(ret, 2 * h);
		// expand to left or right
		while (true) {
			if (i == left && j == right) {
				break;
			}
			if (j == right) { // to left
				h = Math.min(h, heights[--i]);
			} else if (i == left) { // to right
				h = Math.min(h, heights[++j]);
			} else if (heights[i - 1] >= heights[j + 1]) { // to left
				h = Math.min(h, heights[--i]);
			} else if (heights[i - 1] < heights[j + 1]) { // to right
				h = Math.min(h, heights[++j]);
			} else { // catch error
				throw new RuntimeException();
			}
			ret = Math.max(ret, (j - i + 1) * h);
		}
		return ret;
	}
}