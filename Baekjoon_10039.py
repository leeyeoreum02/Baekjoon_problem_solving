# https://www.acmicpc.net/problem/10039

# answer

Wonseop_score = int(input())
SaeHui_score = int(input())
SangGeon_score = int(input())
SoongI_score = int(input())
GangSoo_score = int(input())

score_list = [Wonseop_score, SaeHui_score, SangGeon_score, SoongI_score, GangSoo_score]

for index, score in enumerate(score_list):
    if score < 40:
        score_list[index] = 40
        
mean = int(sum(score_list) / len(score_list))
print(mean)