class Index:
    def get_index(arr, x):
        list_of_indexes = []
        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                if arr[i] + arr[j] == x:
                    list_of_indexes.append([i+1, j+1])
        return list_of_indexes
    
tmp = Index.get_index([10,20,10,40, 50,60,70], 50)
print("List of indices = ", tmp)