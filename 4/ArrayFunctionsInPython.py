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





    if __name__ == "__main__":
        my_list = [101, 303, 404, 505, 707, 100, 100];
        print("Sum of arr elements: ", sum_list(my_list))
        print("Reverse of arr: ", reverse_list(my_list))
    