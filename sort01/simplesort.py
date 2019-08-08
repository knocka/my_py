
def sort(arr):
    i = 0
    j = 0
    min = 0
    for i in range(0, len(arr)-1, 1):
        #print('i:', i)
        min = i
        for j in range(i+1, len(arr), 1):
            #print('j:', j)
            if (arr[min] > arr[j]):
                min = j

        if (min != i):
            arr[i] = arr[i] + arr[min];
            arr[min] = arr[i] - arr[min];
            arr[i] = arr[i] - arr[min];

    return arr

def bubblesort(arr):
    b = len(arr)-1
    for x in range(0,b,1):
        for y in range(0,b-x,1):
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]

    return arr

def main():
    arr = [5, 1, 3, 7, 2, 0, 14, 13, 12]
    print(arr)
    arr = sort(arr)
    print(arr)
    arr1 = [5, 1, 3, 7, 2, 0, 14, 13, 12]
    print(arr1)
    arr1 = bubblesort(arr1)
    print(arr1)

if __name__ == "__main__":
    main()
