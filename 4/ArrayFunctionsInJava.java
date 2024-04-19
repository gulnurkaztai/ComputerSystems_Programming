public class ArrayFunctionsInJava {
    public static long sum_array(int arr[]){
        long res = 0;
        for(int el: arr){
            res +=el;
        }

        return res;
    }



    public static void main(){
        int array[] = {101, 303, 505};
        sum_array(array);
    }
    
}
