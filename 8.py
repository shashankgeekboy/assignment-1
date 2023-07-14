def find_duplicate_and_missing(nums):
  seen = set()
  duplicate = None
  missing = None
  for num in nums:
    if num in seen:
      duplicate = num
    else:
      seen.add(num)
    
  for i in range(1, len(nums) + 1):
    if i not in seen:
      missing = i
  return [duplicate, missing]
nums = [1, 2, 2, 4]

find_duplicate_and_missing(nums)
print(nums)
