class ArrayFunctionsInPython:
    @staticmethod
    def sum_list(list):
        res = 0
        for el in list:
            res+= el
        return res
    
    @staticmethod
    def reverse_list(list):
        j = 0
        res = [0]*len(list)
        for i in range(len(list) -1, -1,-1):
            res[j] = list[i]
            j+=1
        return res
    
    @staticmethod
    def is_polindrome(list_str):
        end = len(list_str) - 1
        for i in range(len(list_str) // 2):
            if list_str[i] != list_str[end - i]:
                return False
        return True
    
    @staticmethod
    def remove_dups(list):
        size = len(list)

        for i in range(size - 1):
            for j in range(size - i - 1):
                if list[j] > list[j+1]:
                    list[j], list[j + 1] = list[j + 1], list[j]

        temp = []
        for i in range(size-1):
            if list[i] != list[i + 1]:
                temp.append(list[i])
        
        temp.append(list[size - 1])
        return temp


    if __name__ == "__main__":
        my_list = [101, 303, 404, 505, 707, 100, 100];
        my_str = ["hello", "world", "and", "world", "hello"]
        print("Sum of arr elements: ", sum_list(my_list))
        print("Reverse of arr: ", reverse_list(my_list))
        print("Is polindrome: ", is_polindrome(my_str))
        print("Array after removing duplicates: ", remove_dups(my_list))