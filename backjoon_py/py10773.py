# -*- coding: utf-8 -*-

# ��� 1
# ���� �Է¹ް� �迭�� append �Ǵ� pop�ϱ�
# pop()�� ������ �迭�� ���� ������

# �ڵ� ----------------------------------
# N = int(input())
# arr = []

# for i in range(0,N):
#     num = int(input())
#     if num == 0 :
#         arr.pop()
#     else :
#         arr.append(num)
# print(sum(arr)) # sum �Լ��� �迭�� ������ ��� ������

# ��� 2 -> �迭���� del�ϱ�

# �ڵ� ----------------------------------
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
arr = [0] * (N+1)

for _ in range(0, N) : 
    arr[cnt] = int(input())
    if arr[cnt] == 0 :
        del arr[cnt-1]
        del arr[cnt]
        cnt -= 1
    else : cnt += 1
    
print(sum(arr))