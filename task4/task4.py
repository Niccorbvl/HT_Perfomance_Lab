import sys

nums = []
with open(file=sys.argv[1], mode="r") as FileNums:
    for line in FileNums:
        nums.append(int(line))
median = sorted(nums)[len(nums)//2]
print(sum(abs(element-median) for element in nums))
