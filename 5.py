def merge_sorted_arrays(nums1, m, nums2, n):
  
  for i in range(m):
    nums1[i + n] = nums1[i]

  i = 0
  j = 0
  k = m

  while i < m and j < n:
    if nums1[k] < nums2[j]:
      nums1[k] = nums1[i]
      i += 1
    else:
      nums1[k] = nums2[j]
      j += 1
    k += 1

  while i < m:
    nums1[k] = nums1[i]
    i += 1
    k += 1

  while j < n:
    nums1[k] = nums2[j]
    j += 1
    k += 1

  return nums1


if __name__ == "__main__":
  nums1 = [1, 2, 3, 0, 0, 0]
  m = 3
  nums2 = [2, 5, 6]
  n = 3

  print(merge_sorted_arrays(nums1, m, nums2, n))
