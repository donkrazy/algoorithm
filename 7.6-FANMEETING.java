import java.util.Arrays;
import java.util.Scanner;

public class FANMEETING {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num_prob = Integer.parseInt(scanner.nextLine());
		while (num_prob-- > 0) {
			int[] members = parseReverse(scanner.nextLine(), true);
			int[] fans = parse(scanner.nextLine());
			System.out.println(solve(members, fans));
		}
		scanner.close();
	}
	
	public static int[] parse(String line){
		int[] ret = new int[line.length()];
		for (int i=0; i<line.length(); i++) {
			if(line.charAt(i) == 'M'){
				ret[i] = 1;
			}
			else{
				ret[i] = 0;
			}
		}
		return ret;
	}

	public static int[] parseReverse(String line, boolean reverse){
		int length = line.length();
		int[] ret = new int[length];
		for (int i=0; i<length; i++) {
			if(line.charAt(i) == 'M'){
				ret[length-1-i] = 1;
			}
			else{
				ret[length-1-i] = 0;
			}
		}
		return ret;
	}
	
	private static int[] add(int[] a, int[] b, int k){
		int length = Math.max(a.length + k, b.length);
		int[] c = new int[length];
		for(int i=0; i<b.length; i++){
			c[i] = b[i];
		}
		for(int i=0; i<a.length; i++){
			c[k + i] = a[i];
		}
		return c;
	}

	private static int[] subtract(int[] a, int[] b){
		for(int i=0; i<b.length; i++){
			a[i] -= b[i];
		}
		normalize(a);
		return a;
	}

	private static void normalize(int[] a){
		for(int i=0; i<a.length; i++){
			if(a[i]<0){
				int borrow = (Math.abs(a[i]) + 9) / 10;
				a[i + 1] -= borrow;
				a[i] += borrow * 10;
			}
			else{
				a[i + 1] += a[i] / 10;
				a[i] = a[i] % 10;
			}
		}
	}
	
	private static int[] multiply(int[] a, int[] b){
		return null;
	}

	private static int[] karatsuba(int[] a, int[] b){
		return null;
	}
	


	private static int solve(int[] members, int[] fans) {
		int count = 0;
		int[] c = karatsuba(members, fans);
		for(int i=members.length; i <= c.length - members.length; i++){
			if(i == 0){
				count++;
			}
		}
		return count;
	}
}
