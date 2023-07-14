def contains_duplicate(nums):
  seen = set()
  for num in nums:
    if num in seen:
      return True
    else:
      seen.add(num)
  return False
nums = [1, 2, 3, 1]
contains_duplicate(nums)
