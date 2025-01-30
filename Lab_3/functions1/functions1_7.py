def has_33(nums):
    i = len(nums) - 1
    while i > 1:
        if nums[i] == 3 and nums[i - 1] == 3:
            print("True")
            return 0
        i -= 1
    print("False")

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])