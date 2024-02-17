def delit(n):
    d = 1
    res = []
    while d ** 2 < n:
        if n % d == 0:
            res.append(d)
            res.append(n // d)
        d += 1
    if d ** 2 == n:
        res.append(d)
    res.sort()
    return res


nums = []
dels = []
for i in range(84052, 84131):
    nums.append(i)
    dels.append(delit(i))

mc = 0
for i in range(len(nums)):
    if len(dels[i]) > mc:
        mc = len(dels[i])
        print(len(dels[i]), nums[i])