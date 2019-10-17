from itertools import product

m,n = map(int, input().split())
m_s = product([str(i) for i in range(1,10)], repeat=m)
print(m_s)
m_nums = [int("".join(i)) for i in m_s]
tot = 0
print(m_nums)
for i in m_nums:
	if i % n ==0:tot+=i;
print(tot)
print("".join(list(str(tot))[::-1]))