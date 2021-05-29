# https://www.acmicpc.net/problem/3003

# answer

chess_piece_list = [1, 1, 2, 2, 2, 8]

piece_list = list(map(int, input().split()))

for index in range(len(chess_piece_list)):
    print(chess_piece_list[index] - piece_list[index], end=' ')