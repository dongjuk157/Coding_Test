N = int(input())
nums = list(map(int, input().split()))
num_dict = {}
for num in sorted(nums):
    if num_dict.get(num) == None:
        num_dict[num] = len(num_dict)
for num in nums:
    print(num_dict[num], end=' ')