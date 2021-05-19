def remove_element(nums, val):
    # create an empty array
    vals = []

    for i in range(len(nums)):
        if nums[i] == val:
            vals.append(nums[i])
    print(len(nums))

def test(did_pass):
    if did_pass:
        res = "test ok"
    else:
        res = "test failed"
    print(res)

def test_suite():
    test(remove_element([3,2,2,3], 2) == 2)

test_suite()

