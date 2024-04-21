class ArrayFunctionsInPython:
    @staticmethod
    def sum_arr(arr):
        res = 0
        for i in arr:
            res+= i
        return res
    
    @staticmethod
    def reverse_arr(arr):
        j = 0
        res = [0]*len(arr)
        for i in range(len(arr) -1, -1,-1):
            res[j] = arr[i]
            j+=1
        return res
    
    @staticmethod
    def is_polindrome(arr_str):
        end = len(arr_str) - 1
        for i in range(len(arr_str) // 2):
            if arr_str[i] != arr_str[end - i]:
                return False
        return True
    
    @staticmethod
    def remove_dups(arr):
        size = len(arr)

        for i in range(size - 1):
            for j in range(size - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        temp = []
        for i in range(size-1):
            if arr[i] != arr[i + 1]:
                temp.append(arr[i])
        
        temp.append(arr[size - 1])
        return temp
    
    @staticmethod
    def move_zeroes(arr):
        j =0
        for i in arr:
            if i != 0:
                arr[j] = i
                j += 1

        for i in range(j, len(arr)):
                arr[i] = 0
        return arr



    if __name__ == "__main__":
        my_arr = [101, 303, 404, 505, 707, 100, 100];
        my_other_arr = [1,5,0,0,7];
        my_str = ["hello", "world", "and", "world", "hello"]
        print("Sum of arr elements: ", sum_arr(my_arr))
        print("Reverse of arr: ", reverse_arr(my_arr))
        print("Is polindrome: ", is_polindrome(my_str))
        print("Array after removing duplicates: ", remove_dups(my_arr))
        print("Array with zeroes at the end: ", move_zeroes(my_other_arr))