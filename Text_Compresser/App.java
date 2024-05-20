package Text_Compresser;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

public class App {
    public static void main(String[] args){
        try (FileReader in = new FileReader("./Text_Compresser/input.txt");
             FileWriter out = new FileWriter("output_java.sc")) {
            
            Map<String, Integer> wordHashMap = new LinkedHashMap<>();
            int index = 1;
            int data;
            StringBuilder wordBuilder = new StringBuilder();
            while ((data = in.read()) != -1){
                char c = (char) data;
                if(Character.isWhitespace(c)){
                    String word = wordBuilder.toString();
                    wordBuilder.setLength(0);
                    if(!word.isEmpty()){
                        wordHashMap.putIfAbsent(word, index++);
                        out.write(wordHashMap.get(word)+ " ");
                    }
                } else {
                    wordBuilder.append(c); 
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

