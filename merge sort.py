# merge sort
import sys

class Program:
    def __init__(self):
        self.list_input = input("Enter a list of of items to be sorted seperated by commas e.g 1,2,3 or a,b,c,d:")
        self.list = self.list_input.split(",")
        print(self.list)
        self.list_type = input("Do you want to sort a list of text, numbers, or decimals: ")
        self.list_type = self.list_type.strip()
        self.list_type = self.list_type.lower()
        match self.list_type:
            case "t":
                self.list_type = "string"
            case "text":
                self.list_type = "string"
            case "texts":
                self.list_type = "string"
            case "n":
                self.list_type = "number"
            case "number":
                self.list_type = "number"
            case "numbers":
                self.list_type = "number"
            case "d":
                self.list_type = "decimal"
            case "decimal":
                self.list_type = "decimal"
            case "decimals":
                self.list_type = "decimal"
            case _:
                print("We could not identify the type of list please re-run and try again...")
                sys.exit()

        print(self.list_type + " sort type has been selected")

        if self.list_type == "number":
            self.list = [int(item.strip()) for item in self.list]
        elif self.list_type == "decimal":
            self.list = [float(item.strip()) for item in self.list]

    def display_result(self):
        print(self.list)

    def merge_sort(self,list_to_sort):
        if len(list_to_sort) > 1:
            # divide
            left_list = list_to_sort[:len(list_to_sort)//2]
            right_list = list_to_sort[len(list_to_sort)//2:]

            # recursion
            self.merge_sort(left_list)
            self.merge_sort(right_list)

            # merge
            i = 0 # left array index
            j = 0 # right array index
            k = 0 # merge array index
            while i < len(left_list) and j < len(right_list):
                if left_list[i] < right_list[j]:
                    list_to_sort[k] = left_list[i]
                    i += 1
                else:
                    list_to_sort[k] = right_list[j]
                    j += 1
                k += 1

            while i < len(left_list):
                list_to_sort[k] = left_list[i]
                i += 1
                k += 1

            while j < len(right_list):
                list_to_sort[k] = right_list[j]
                j += 1
                k += 1   
                
program1 = Program()
program1.merge_sort(program1.list)
program1.display_result()
