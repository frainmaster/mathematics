import math

eg = []
print('enter a number')
x = int(input())
print('a^2\t+\tb^2\t=\tc^2')
for a in range (1, x):
    for b in range (1, x):
        h = math.sqrt(a*a + b*b)
        if (h - int(h) == 0):
            if (a < b):
                j = b/a
                if j not in eg:
                    eg.append(float(j))
                    print(str(a) + '\t \t' + str(b) + '\t \t' + str(int(h)))
