# 가로 방향으로 6칸, 세로 방향으로 5칸인 직사각형 모양의 길의 경로의 수 구하기

M, N = 6, 5 # 가로, 세로의 길이

route = [[0 for i in range(N+1)] for j in range (M+1)]

# 가로 방향의 첫 1행을 설정
for i in range(M + 1):
    route[i][0] = 1

for i in range(1, N + 1):
    # 세로 방향의 첫 1열을 설정
    route[0][i] = 1
    for j in range(M + 1):
        # 왼쪽과 아래뽁의 교차점에 적혀 있는 숫자를 더함
        route[j][i] = route[j - 1][i] + route[j][i - 1]

print(route[M][N])