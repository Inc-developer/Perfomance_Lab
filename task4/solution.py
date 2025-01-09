import sys


def calc_ways(array_file):
    with open(array_file, "r") as file:
        nums = list(file)
        nums = [int(i.rstrip()) for i in nums]
    nums.sort()
    mid = (nums[0] + nums[-1]) // 2
    counter = 0
    while nums[0] - nums[-1] != 0:
        for i in range(len(nums)):
            if nums[i] < mid:
                counter += 1
                nums[i] += 1
            if nums[i] > mid:
                counter += 1
                nums[i] -= 1
    return counter


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(calc_ways(sys.argv[1]))
    else:
        print("Need 1 arg (file path)")