import java.util.Scanner;

public class FanMeeting {

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

	private static int count(String[] members, String[] fans) {
		int ret = 0;
		int numMember = members.length;
		int numFan = fans.length;
		for (int i = 0; i <= numFan - numMember; i++) {
			boolean embarrased = false;
			for (int j = 0; j < numMember; j++) {
				if (members[j].equals("M") && fans[i + j].equals("M")) {
					embarrased = true;
				}
			}
			if (embarrased) {
				continue;
			}
			else {
				ret++;
			}
		}
		return ret;
	}
}
