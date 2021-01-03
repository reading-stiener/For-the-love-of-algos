import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.math.BigDecimal;

public class Main {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in);
    BufferedReader in = new BufferedReader(reader);

    try {
        double purchasePrice = Double.parseDouble(in.readLine());
        double cash = Double.parseDouble(in.readLine());
        CashRegister x = new CashRegister();
        //System.out.println(x);
        //Main.calculateChange(purchasePrice, cash);
        System.out.println(x.computeChange(purchasePrice, cash));
    } catch (Exception e) {
        System.out.println(e);
    }
  }

  // public static void calculateChange(double purchasePrice, double cash) {
  //   // Access your code here. Feel free to create other classes as required
  //   System.out.println(1);
  // }
}
  class CashRegister { 
    Map<Double, String> availbleCash = new HashMap<>() {{ 
      put(0.01, "One Pence");
      put(0.02, "Two Pence");
      put(0.05, "Five Pence");
      put(0.10, "Ten Pence");
      put(0.20, "Twenty Pence");
      put(0.50, "Fifty Pence"); 
      put(1.0, "One Pound");
      put(2.0,  "Two Pounds");
      put(5.0, "Five Pounds");
      put(10.0, "Ten Pounds");
      put(20.0, "Twenty Pounds"); 
      put(50.0, "Fifty Pounds");
    }};
    public CashRegister() { 
      this.availbleCash = availbleCash;
    }
    public String toString() { 
      return this.availbleCash.toString();
    }
    public String computeChange(double purchasePrice, double cash) {
      StringBuilder changeString = new StringBuilder();
      java.math.BigDecimal cashReturn = BigDecimal.valueOf(cash - purchasePrice); 
      if (cashReturn.doubleValue() < 0) { 
        return "ERROR";
      } else if (cash == purchasePrice) { 
        return "0";
      } else { 
        double[] denoms = new double[] {50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01};
        //System.out.println(cashReturn);
        for (int i = 0; i < denoms.length; i++) { 
          while (cashReturn.doubleValue() >= denoms[i]) {
            //System.out.println(cashReturn);
            cashReturn = cashReturn.subtract(BigDecimal.valueOf(denoms[i]));
            if (cashReturn.doubleValue() == 0) { 
              changeString.append(this.availbleCash.get(denoms[i]));
            } else { 
              changeString.append(this.availbleCash.get(denoms[i]) + ", ");
            }
            
          }
        }
      }
      return changeString.toString();
    }
  } 