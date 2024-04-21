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

    public static int[] remove_dups(int arr[]) {
        int size = arr.length;

        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    
        int[] temp = new int[size];
        int j = 0;
    
        for (int i = 0; i < size - 1; i++) {
            if (arr[i] != arr[i + 1]) {
                temp[j++] = arr[i];
            }
        }
        temp[j++] = arr[size - 1];

        int[] uniqueElements = new int[j];
        System.arraycopy(temp, 0, uniqueElements, 0, j);

    
        return uniqueElements;
    }

    public static int[] move_zeroes(int[] arr){
        int j = 0;
        for(int i : arr){
            if(i != 0){
                arr[j++] = i;
            }
        }

        if(j<arr.length){
            for(int i = j; i<arr.length;i++){
                arr[i] = 0;
            }
        }
        return arr;
    }
    

    public static void main(String[] args){
        int array[] = {101, 303, 404, 505, 707, 100, 100};
        int arr[] = {1,5,0,0,7};
        String[] str_arr = {"hello", "world", "and", "world", "hello"};
        System.out.println("Sum of arr elements: " + sum_array(array));

        System.out.println("Reverse of arr: " + Arrays.toString(reverse_array(array)));
        
        System.out.println("Is polindrome: " + is_polindrome(str_arr));

        System.out.print("Array after removing duplicates: " + Arrays.toString(remove_dups(array)));

        System.out.println("Array with zeroes at the end: " + Arrays.toString(move_zeroes(arr)));
    }
    
}
