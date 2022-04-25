import copy

class Set:
    def __init__(self) -> None:
        self.current_list = []
    def generateSets(self, full_arr, curr_subset, index):
        self.current_list.append(copy.copy(curr_subset))
        for i in range(index, len(full_arr)):
            curr_subset.append(full_arr[i])
            self.generateSets(full_arr, curr_subset, i + 1)
            curr_subset.pop(-1)
        return
    def printSets(self):
        print(self.current_list)

s = Set()
s.generateSets([4,5,6], [], 0)
s.printSets()

