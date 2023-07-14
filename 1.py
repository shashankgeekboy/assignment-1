def two_sum(nums, target):
  seen = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
      return [i, seen[complement]]
    else:
      seen[num] = i

  return []
nums = [2, 7, 11, 15]
target = 9

indices = two_sum(nums, target)
print(indices)
