import sys


def minimumSwaps(arr):
    # initialize the swap count
    swap_count = 0
    # create a dictionary that contains the value and it's index as key value pairs
    index_dictionary = dict(zip(arr, range(1, len(arr)+1)))
    
    # loop through the array
    for i in range(1, len(arr)+1):
        # check if the current value (i) is equal to the index in the dictionary
        if index_dictionary[i] != i:
            # swap the next value in the dictionary to the current value
            index_dictionary[arr[i-1]] = index_dictionary[i]
            arr[index_dictionary[i]-1] = arr[i-1]
            swap_count += 1
            

    print("final count", swap_count)        
    return swap_count

            
def test(did_pass):
    if did_pass:
        response = "Test Ok"
    else:
        response = "Test failed"
    print(response)


def test_suite():
    test(minimumSwaps([2, 3, 4, 1, 5]) == 3)
    test(minimumSwaps([4, 3, 1, 2]) == 3)

test_suite()

