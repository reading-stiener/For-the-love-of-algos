import java.util.Arrays;
public class Main {
    public static void testPrint(String statement) { 
        System.out.println(statement);
    }
    void testPrint1(String statement) { 
        System.out.println(statement);
    }
    public static int sum(int x) { 
        if (x == 0) { 
            return 0;
        } else {
            return x + sum(x-1);
        }
    }
    public static void main(String[] args) {
        int myInt = 9;
        double myDouble = myInt; // Automatic casting: int to double
    
        System.out.println(myInt);      // Outputs 9
        System.out.println(myDouble);   // Outputs 9.0
        String[] cars = {"BMW", "Tesla", "Porsche"};
        for (String car : cars) { 
            System.out.println(car);
        }
        System.out.println(Arrays.toString(cars));
        // statically reference methods
        testPrint("Say hello!");

        // reference functions through objects
        Main s = new Main();
        s.testPrint1("Say hello");


        // call say hello 3 three times 
        for (int i = 0; i < 3; i++) { 
            System.out.println(i);
            testPrint("yoyo");
        }
        System.out.println(sum(5));

    }
}