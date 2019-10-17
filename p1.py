m, n = map(int, input().split())
u = set()
for i in range(m, n):
	if i == 1:
		u.add(i)
	if i > 1:
		for j in range(2,i):
			if i % j == 0:
				break
		else:
			u.add(i)
print(sum(list(u)))

t = sum(list(u))
s = range(1,n)
l = [s[i:j] for i in range(len(s))
		for j in range(i+1,len(s)+1)]
lst = []
lst_c = 0
for i in l:
	if sum(i) == t:
		lst.append(i)
		lst_c += 1
for i in lst:
	print(" ".join([str(j) for j in i]))
print(lst_c)