package Text_Compresser;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class App {
    public static void main(String[] args){
        try (FileReader in = new FileReader("./Text_Compresser/input.txt");
             FileWriter out = new FileWriter("output_java.sc")) {
            int c;
            while ((c = in.read()) != -1){
                out.write(c);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

