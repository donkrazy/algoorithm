import java.util.Arrays;
import java.util.Scanner;

public class FANMEETING {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num_prob = Integer.parseInt(scanner.nextLine());
		while (num_prob-- > 0) {
			int[] members = parse(scanner.nextLine());
			int[] fans = parseReverse(scanner.nextLine(), true);
			System.out.println(solve(members, fans));
		}
		scanner.close();
	}

	private static int solve(int[] members, int[] fans) {
		int count = 0;
		int[] c = karatsuba(members, fans);
		for (int i = members.length - 1; i < fans.length; i++) {
			if (c[i] == 0) {
				count++;
			}
		}
		return count;
	}

	private static int[] karatsuba(int[] a, int[] b) {
		// 1) base cases
		if (a.length > b.length) {
			return karatsuba(b, a);
		}
		if (a.length == 0 || b.length == 0) {
			return new int[] { 0 };
		}
		if (a.length < 50) {
			return multiply(a, b);
		}

		// 2) split: a = a0 + a1; b = b0 + b1;
		int half = a.length / 2;
		int[] a0 = Arrays.copyOfRange(a, 0, half);
		int[] a1 = Arrays.copyOfRange(a, half, a.length);
		int[] b0 = Arrays.copyOfRange(b, 0, Math.min(half, b.length));
		int[] b1 = Arrays.copyOfRange(b, Math.min(half, b.length), b.length);

		// 3) z0 = a0 * b0; z2 = a1 * b1;
		// z1 = (a0 + a1) * (b0 + b1) - z0 - z2;
		int[] z0 = karatsuba(a0, b0);
		int[] z2 = karatsuba(a1, b1);
		int[] z1 = subtract(subtract(karatsuba(add(a0, a1, 0), add(b0, b1, 0)), z0), z2);

		// 4) a * b = z0 + z1 * 10^n + z2 * 10 ^ 2n
		int[] c = add(add(z0, z1, half), z2, 2 * half);
		return c;
	}

	public static int[] parse(String line) {
		int[] ret = new int[line.length()];
		for (int i = 0; i < line.length(); i++) {
			if (line.charAt(i) == 'M') {
				ret[i] = 1;
			} else {
				ret[i] = 0;
			}
		}
		return ret;
	}

	public static int[] parseReverse(String line, boolean reverse) {
		int length = line.length();
		int[] ret = new int[length];
		for (int i = 0; i < length; i++) {
			if (line.charAt(i) == 'M') {
				ret[length - 1 - i] = 1;
			} else {
				ret[length - 1 - i] = 0;
			}
		}
		return ret;
	}

	private static int[] add(int[] a, int[] b, int k) {
		int aLen = a.length;
		int bLen = b.length;
		int cLen = Math.max(aLen + k, bLen);
		int[] c = new int[cLen];
		for (int i = 0; i < bLen; i++) {
			c[cLen - 1 - i] = b[bLen - 1 - i];
		}
		for (int i = 0; i < aLen; i++) {
			c[cLen - 1 - i - k] += a[aLen - 1 - i];
		}
		return c;
	}

	private static int[] subtract(int[] a, int[] b) {
		// a.length > b.length
		for (int i = 0; i < b.length; i++) {
			a[a.length - 1 - i] -= b[b.length - 1 - i];
		}
		return a;
	}

	private static int[] multiply(int[] a, int[] b) {
		int length = a.length + b.length - 1;
		int[] c = new int[length];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < b.length; j++) {
				c[i + j] += a[i] * b[j];
			}
		}
		return c;
	}
	
//  안필요함
//	private static int[] normalize(int[] a) {
//		for (int i = a.length - 1; i > 0; i--) {
//			if (a[i] < 0) {
//				int borrow = (Math.abs(a[i]) + 9) / 10;
//				a[i - 1] -= borrow;
//				a[i] += borrow * 10;
//			} else {
//				a[i - 1] += a[i] / 10;
//				a[i] = a[i] % 10;
//			}
//		}
//		if (a[0] >= 10) {
//			// TODO: 최고자리수 올림
//		}
//		if (a[0] == 0) {
//			// TODO: 앞의 0 다 없애기
//		}
//		return a;
//	}
}
