import java.util.Arrays;

public class ArrayFunctionsInJava {
    public static long sum_array(int arr[]){
        long res = 0;
        for(int el: arr){
            res +=el;
        }

        return res;
    }

    public static int[] reverse_array(int arr[]){
        int j = 0;
        int[] res  = new int[arr.length];
        for(int i = arr.length - 1; i >=0; i --){
            res[j] = arr[i];
            j++;
        }
        return res;
    }

    public static boolean is_polindrome(String arr[]){
        int end = arr.length - 1;
        for(int i=0; i<arr.length/2; i++){
            if(!arr[i].equals(arr[end-i])){
                return false;
            }
        }

        return true;
    }


    public static void main(String[] args){
        int array[] = {101, 303, 404, 505, 707};
        String[] str_arr = {"hello", "world", "and", "world", "hello"};
        System.out.println("Sum of arr elements: " + sum_array(array));

        System.out.println("Reverse of arr: " + Arrays.toString(reverse_array(array)));
        
        System.out.println("Is polindrome: " + is_polindrome(str_arr));
    }
    
}
