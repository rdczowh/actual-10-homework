l = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
for j in range(2):
	for i in range(len(l)-j-1):
		if l[i+1] < l[i]:
			l[i], l[i+1] = l[i+1], l[i]

print l[:-3:-1]