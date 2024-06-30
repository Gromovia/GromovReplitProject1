def all_pairs(a, target):
  a.sort()
  n = len(a)
  res = []
  for i in range(0, n-1):
      for j in range(i+1, n):
          if a[i]+a[j]==target:
              res.append([a[i],a[j]])
  return res