file = open('24_58329.txt')
s = file.readline()

c = 0
mc = 0
for i in range(len(s)-2):
    if int(s[i]) + int(s[i+1]) > int(s[i+2]):
        c += 1
        mc = max(c + 2, mc)
    else:
        c = 0
print(mc)