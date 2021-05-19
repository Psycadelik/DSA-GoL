import sys


def minimumSwaps(arr):
    print(arr)
    count = 0
    for i in range(len(arr)):
        if i > i+1:
    

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
