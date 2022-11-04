import java.lang.Math;
public class Calculator {

    private static float add(int a, int b) {
        return a + b;
    }
    private static float subtract(int a, int b) {
        return a - b;
    }

    private static float multiply(int a, int b){
        return a * b;
    }

    private static float divide(float a, float b){
        return a / b;
    }

    private static double square(int a){
        return Math.pow(a,2);
    }

    private static double cube(int a){
        return Math.pow(a,3);
    }

    private static double power(int a, int b){
        return Math.pow(a,b);
    }

    public static void main(String[] args) {
        String method = args[0];
        int a = Integer.parseInt(args[1]);
        int b = Integer.parseInt(args[2]);
        System.out.println("Please enter one of the operators below (word not symbol) and number(s) you want to use.");
        System.out.println("Operations: add (a+b)");
        System.out.println("Operations: subtract (a-b)");
        System.out.println("Operations: multiply (a*b)");
        System.out.println("Operations: divide (a/b)");
        System.out.println("Operations: square (a^2)");
        System.out.println("Operations: cube (a^3)");
        System.out.println("Operations: power (a^b)");
        switch (method) {
            case "add":
                System.out.println(add(a, b));
                break;
            case "subtract":
                System.out.println(subtract(a, b));
                break;
            case "multiply":
                System.out.println(multiply(a, b));
                break;
            case "divide":
                System.out.println(divide(a, b));
                break;
            case "square":
                System.out.println(square(a));
                break;
            case "cube":
                System.out.println(cube(a));
                break;
            case "power":
                System.out.println(power(a, b));
                break;
            default:
                System.out.print("Please enter a valid operator and/or numbers.");
                break;
        }
    }
}
