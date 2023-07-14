def remove_val(nums, val):
  i = 0
  k = 0
  while i < len(nums):
    if nums[i] != val:
      nums[k] = nums[i]
      k += 1
    i += 1

  return k
nums = [1, 2, 3, 2, 3, 1, 2, 3]
val = 2

k = remove_val(nums, val)

print(nums[:k])
