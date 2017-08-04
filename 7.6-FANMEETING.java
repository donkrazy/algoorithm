import java.util.Scanner;

public class FANMEETING {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num_prob = Integer.parseInt(scanner.nextLine());
		while (num_prob-- > 0) {
			String[] members = scanner.nextLine().split("");
			String[] fans = scanner.nextLine().split("");
			System.out.println(count(members, fans));
		}
		scanner.close();
	}

	//TODO
	private static int[] add(int[]a, int[] b){
		return null;
	}

	private static void subtract(int[] a, int[] b){

	}

	private static void normalize(int[] a){

	}

	private static int[] karatsuba(int[] a, int[] b){
		return null;
	}

	private static int count(String[] members, String[] fans) {
		int count = 0;
		int[] c = karatsuba(a, b);
		for(int i=b.length; i <= c.length - b.length; i++){
			if(i == 0){
				count++;
			}
		}
		return count;
	}
}
