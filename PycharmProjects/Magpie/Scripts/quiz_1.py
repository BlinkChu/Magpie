from random import randint,seed
n=20;m=30;p=40;
seed(10)
A=[[[randint(-1,1) for x in range(n)] for y in range(m)] for z in range(p)]
print(A)

count_1 = 0
count_11 = 0
count_0 = 0
for i_1 in range(p):
    for i_2 in range(m):
        count_1 += A[i_1][i_2].count(1)
        count_11 += A[i_1][i_2].count(-1)
        count_0 += A[i_1][i_2].count(0)

print(count_0)
print(count_1)
print(count_11)