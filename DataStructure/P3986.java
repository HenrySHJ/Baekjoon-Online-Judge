import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class P3986 {
    static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int N = Integer.parseInt(scan.next());
        int ans = 0;

        for (int i = 0; i < N; i++) {
            Deque<Character> stack = new ArrayDeque<>();
            String word = scan.next();

            for (int j = 0; j < word.length(); j++) {
                char w = word.charAt(j);

                if (!stack.isEmpty() && stack.peek() == w) {
                    stack.pop();
                }

                else {
                    stack.push(w);
                }
            }

            if (stack.isEmpty()) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}
