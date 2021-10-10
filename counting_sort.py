import shutil
columns = shutil.get_terminal_size().columns

def Counting_Sort(A, k):
 
    # create an integer list of size `n` to store the sorted list
    output = [0] * len(A)
    #[0, 0, 0, 0, 0, 0, 0, 0, 0]
 
    # create an integer list of size `k + 1`, initialized by all zero
    freq = [0] * (k + 1)
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 
    # using the value of each item in the input list as an index,
    # store each integer's count in `freq[]`
    for i in A:
        freq[i] = freq[i] + 1
        #[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] - 4
        #[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0] - 2
        #[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1] - 10
        #[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2] - 10
        #[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 2] - 1
        #[0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 2] - 4
        #[0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 2] - 2
        #[0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 2] - 1
        #[0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 3] - 10
 
    # calculate the starting index for each integer
    total = 0
    for i in range(k + 1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount
        #[0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 3] - 0
        #0 -> 0 (nothing changes) -> total = 0+0
        #[0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 3] - 1
        #2 -> [0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 3] -> total = 2
        #[0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 3] - 2
        #2 -> 2 (nothing changes) -> total = 4
        #[0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 3] - 3
        #0 -> [0, 0, 2, 4, 2, 0, 0, 0, 0, 0, 3] -> total = 4
        #[0, 0, 2, 4, 2, 0, 0, 0, 0, 0, 3] - 4
        #2 -> [0, 0, 2, 4, 4, 0, 0, 0, 0, 0, 3] -> total = 6
        #[0, 0, 2, 4, 4, 0, 0, 0, 0, 0, 3] - 5
        #0 -> [0, 0, 2, 4, 4, 6, 0, 0, 0, 0, 3] -> total = 6
        #[0, 0, 2, 4, 4, 6, 0, 0, 0, 0, 3] - 6
        #0 -> [0, 0, 2, 4, 4, 6, 6, 0, 0, 0, 3] -> total = 6
        #[0, 0, 2, 4, 4, 6, 6, 0, 0, 0, 3] - 7
        #0 -> [0, 0, 2, 4, 4, 6, 6, 6, 0, 0, 3] -> total = 6        
        #[0, 0, 2, 4, 4, 6, 6, 6, 0, 0, 3] - 8
        #0 -> [0, 0, 2, 4, 4, 6, 6, 6, 6, 0, 3] -> total = 6
        #[0, 0, 2, 4, 4, 6, 6, 6, 6, 0, 3] - 9
        #0 -> [0, 0, 2, 4, 4, 6, 6, 6, 6, 6, 3] -> total = 6
        #[0, 0, 2, 4, 4, 6, 6, 6, 6, 6, 3] - 10
        #3 -> [0, 0, 2, 4, 4, 6, 6, 6, 6, 6, 6] -> total = 9

 
    # copy to the output list, preserving the order of inputs with equal keys
    for i in A:
        output[freq[i]] = i
        freq[i] = freq[i] + 1
        #[0, 0, 0, 0, 4, 0, 0, 0, 0] - 4
        #[0, 0, 2, 4, 5, 6, 6, 6, 6, 6, 6]
        #[0, 0, 2, 0, 4, 0, 0, 0, 0] - 2
        #[0, 0, 3, 4, 5, 6, 6, 6, 6, 6, 6]
        #[0, 0, 2, 0, 4, 0, 10, 0, 0] - 10
        #[0, 0, 3, 4, 5, 6, 6, 6, 6, 6, 7]
        #[0, 0, 2, 0, 4, 0, 10, 10, 0] - 10
        #[0, 0, 3, 4, 5, 6, 6, 6, 6, 6, 8]
        #[1, 0, 2, 0, 4, 0, 10, 10, 0] - 1
        #[0, 1, 3, 4, 5, 6, 6, 6, 6, 6, 8]
        #[1, 0, 2, 0, 4, 4, 10, 10, 0] - 4
        #[0, 1, 3, 4, 6, 6, 6, 6, 6, 6, 8]
        #[1, 0, 2, 2, 4, 4, 10, 10, 0] - 2
        #[0, 1, 4, 4, 6, 6, 6, 6, 6, 6, 8]
        #[1, 1, 2, 2, 4, 4, 10, 10, 0] - 1
        #[0, 2, 4, 4, 6, 6, 6, 6, 6, 6, 8]
        #[1, 1, 2, 2, 4, 4, 10, 10, 10] - 1      - output array (already sorted)
        #[0, 2, 4, 4, 6, 6, 6, 6, 6, 6, 9]       - freq array

 
    # copy the output list back to the input list
    for i in range(len(A)):
        A[i] = output[i]

    #A = [4, 2, 10, 10, 1, 4, 2, 1, 10]
    #output = [1, 1, 2, 2, 4, 4, 10, 10, 10]
    #A = [1, 1, 2, 2, 4, 4, 10, 10, 10] - sorted
    return A
 
 
if __name__ == '__main__':

    print("COUNTING SORT".center(columns))
    while True:
        array = input("\nInput integers separated by commas: ").split(",")
        array = [int(x) for x in array]
        k = int(input("\nInput the maximum value of the array: "))

        print(Counting_Sort(array, k))

        ask = input("\nWanna Continue? [y/n]: ").lower()
        if ask == "y":
            continue
        elif ask == "n":
            exit()
        

"""
Explanation:
- Given range of values in the array - k
- And an array of ints with size n where the ints might repeat - A
- Sort this array 
- It works similar to adjecancy list 
  1. use the values of list A as indecies for list B, and the values to those elements you put the total number of counts of that value in the array A.
  2. apply the following formula to transform array B to array C: 
- as you visit each index, assign total to it, then update total as the previous value plus total. 
- Start total as 0, and remember the current value of counts at the beginning of each iteration.
"    total = 0
    for i in range(k + 1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount
"
  3. Apply each value of array A as index to array C to get the index for this A value and put in in the final array D.
  4. record array D to array A
"""

