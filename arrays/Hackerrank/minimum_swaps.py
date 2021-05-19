import sys


def minimumSwaps(arr):
    count = 0
    # loop through the array
    for i in range(0, len(arr)-1):
        # check if current index value is greater than the next index value
        if arr[i] != arr[i+1]:
            # increase counter
            count += 1
            # assign the value to a temp variable
            temp = arr[i]
            # swap the value in the next index to current index
            arr[i] = arr[i+1]
            # assign the value stored in temp to the next index
            arr[i+1] = temp

    print("final count", count)        
    return count

            
def test(did_pass):
    if did_pass:
        response = "Test Ok"
    else:
        response = "Test failed"
    print(response)


def test_suite():
    test(minimumSwaps([2, 3, 4, 1, 5]) == 5)
    test(minimumSwaps([4, 3, 1, 2]) == 4)

test_suite()

