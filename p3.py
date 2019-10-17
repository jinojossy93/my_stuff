Arr = "100 496 152 190 490 742 173".split()
A = "100"
B = "496"
c_A = list(A)
c_B = list(B)
u = set()
for i in range(len(Arr)):
	for i, j in enumerate(c_B):
		CA= c_A.copy()
		CA[i] = j
		if "".join(CA) in Arr and "".join(CA) not in list(u):
			c_A[i] = j
			u.add("".join(CA))
			print("".join(CA))
			break
# options = ["".join() for i in c_B]