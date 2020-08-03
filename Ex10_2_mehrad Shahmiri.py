import numpy as np
import matplotlib.pyplot as plt
vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]])
#1
vec2 = (np.pi/4) * vec1
#2
vec2 = np.cos( vec2 )
#3
vec3 = vec1 + 2 * vec2
#5
vec4=vec3*mat1
#6
m=np.transpose(mat1)
#7
d=np.linalg.det(mat1)
#8
t=np.trace(mat1)
#9
miv=np.min(vec1)
#10
ind=np.where(vec1 == np.min(vec1))
#11
mim=np.min(mat1)
#12
A=np.array([[17, 24, 1, 8, 15],
[23, 5, 7, 14, 16],
[ 4, 6, 13, 20, 22],
[10, 12, 19, 21, 3],
[11, 18, 25, 2, 9]])

c=np.min(np.sum(A,axis=1))== np.max(np.sum(A,axis=1))==np.min(np.sum(A,axis=0))==np.max(np.sum(A,axis=0))==np.sum(np.log(np.diagonal(A)))
print(c)
#13
M=np.random.rand(10,10)
print(M)
#14
MUL=M[:5,:5]
MUR=M[:5,6:]
MLL=M[6:,:5]
MLR=M[6:,6:]

