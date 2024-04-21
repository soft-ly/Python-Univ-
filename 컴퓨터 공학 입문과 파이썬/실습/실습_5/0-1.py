A={2,4,5}
B={1,2,2,1,10,4}
C={3,3,3,4}
print(A&B&C)
print(A.intersection(B).intersection(C))
print((A|B|C)-A)
print(A.union(B).union(C).difference(A))
