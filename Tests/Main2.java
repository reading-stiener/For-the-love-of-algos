import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.math.BigDecimal;

public class Main2 {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    try { 
        while ((line = in.readLine()) != null) {
            //Main.matchBenchmark(line);
            PortfolioBenchMark test = new PortfolioBenchMark(line);
            test.matchBenchmark();
            //System.out.println(test);
        }
    } catch (Exception e) {
        System.out.println(e);
    }
  }
  
  public static void matchBenchmark(String input) {
    // Access your code here. Feel free to create other classes as required
  }
}
class PortfolioBenchMark { 
    Map<String, Double> portfolio = new HashMap<>();
    Map<String, Double> benchmark = new HashMap<>();
    public PortfolioBenchMark(String input) {
        String[] inputSplit = input.split(":");
        // Setting up portfolio hashmap
        String[] portfolioList = inputSplit[0].split("\\|");
        for (String str : portfolioList) {
            String[] stockOrBond = str.split(",");
            portfolio.put(stockOrBond[0]+","+stockOrBond[1], Double.parseDouble(stockOrBond[2]));
        }
        //Setting up BenchMark hashmap
        String[] benchmarkList = inputSplit[1].split("\\|");
        for (String str : benchmarkList) { 
            String[] stockOrBond = str.split(",");
            benchmark.put(stockOrBond[0]+","+stockOrBond[1], Double.parseDouble(stockOrBond[2]));
        }
        //System.out.println(portfolio.toString());
        //System.out.println(benchmark.toString());
    }
    public void matchBenchmark() {
        Map <String, Double> finalList = new HashMap<>();
        // Get the iterator over the benchmark HashMap 
        Iterator<Map.Entry<String, Double>> it = this.benchmark.entrySet().iterator(); 
        while (it.hasNext()) {
            Map.Entry<String, Double> entry = it.next(); 
            Double portValue = portfolio.get(entry.getKey()); 
            if (portValue != null) { 
                finalList.put(entry.getKey(), entry.getValue() - portValue); 
            } else { 
                finalList.put(entry.getKey(), entry.getValue());
            }
            portfolio.remove(entry.getKey());
            it.remove();
        }
        
        // Iterator for remaining portfolio HashMap
        Iterator<Map.Entry<String, Double>> ite = this.portfolio.entrySet().iterator();
        while (ite.hasNext()) { 
            Map.Entry<String, Double> entry = ite.next();
            finalList.put(entry.getKey(), -entry.getValue());
            ite.remove();
        }

        // Sort the result and return string on terminal

        TreeMap<String, Double> sorted = new TreeMap<>(); 
        // Copy all data from hashMap into TreeMap 
        sorted.putAll(finalList);
        for (Map.Entry<String, Double> entry: sorted.entrySet()) {
            if (entry.getValue() > 0) {

                System.out.println("BUY,"+entry.getKey()+","+ BigDecimal.valueOf(entry.getValue()).stripTrailingZeros().toPlainString());
            } else if (entry.getValue() < 0) { 
                System.out.println("SELL,"+entry.getKey()+","+ BigDecimal.valueOf(entry.getValue()*-1).stripTrailingZeros().toPlainString());
            }
        }
    }  
}