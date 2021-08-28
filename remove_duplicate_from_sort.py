def removeDuplicates(nums):
    nums[:] = set(nums)
    nums.sort()
    print(nums)
    return len(nums)


def main():
    removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    removeDuplicates([1, 1, 2])


main()
