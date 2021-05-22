def remove_element(nums, val):
    k = 0
    lens = 0
    # create an empty array
    vals = []

    for i in range(len(nums)):
        if nums[i-k] == val:
            nums.append(val)
            nums.pop(i-k)
            k += 1
        else:
            lens += 1
    return lens

def test(did_pass):
    if did_pass:
        res = "test ok"
    else:
        res = "test failed"
    print(res)

def test_suite():
    test(remove_element([3,2,2,3], 3) == 2)

test_suite()

