import java.util.Scanner;

public class P1316 {
    static Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {

        int count = 0;
        int N = scan.nextInt();

        for (int i = 0; i < N; i++) {
            if (check() == true) {
                count++;
            }
        }
        System.out.println(count);
    }

    public static boolean check() {
        boolean[] check = new boolean[26];
        int prev = 0;
        String str = scan.next();

        for (int i = 0; i < str.length(); i++) {
            int now = str.charAt(i);

            // 이전 숫자와 현재 숫자의 ASCII를 비교
            if (prev != now) {
                // 최초로 확인된 문자인 경우 처리 & True 반환
                if (check[now - 'a'] == false) {
                    check[now - 'a'] = true;
                    prev = now;
                }
                // 이미 확인된 문자인 경우 False 반환
                else {
                    return false;
                }
            }
        }
        return true;
    }
}
