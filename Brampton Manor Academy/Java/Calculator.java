public class Calculator {

    private static int addition(int a, int b) {
        int answer = a + b;
        return answer;
    }

    private static int  subtract(int a, int b) {
        int answer = a - b;
        return answer;
    }

    public static void main(String[] args) {
        int firstValue = Integer.parseInt(args[0]);
        int secondValue = Integer.parseInt(args[1]);
        int answer = addition(firstValue, secondValue);
        System.out.println(answer);
    }
}
