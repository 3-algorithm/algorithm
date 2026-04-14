import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [False] * n
nums = [0] * m
result_set = set()
output = []

def backtrack(depth):
    if depth == m:
        # 현재 완성된 수열을 문자열이나 튜플로 만들어 중복 체크
        current_seq = tuple(nums)
        if current_seq not in result_set:
            result_set.add(current_seq)
            output.append(" ".join(map(str, nums)))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            nums[depth] = arr[i]
            backtrack(depth + 1)
            visited[i] = False

backtrack(0)
print("\n".join(output))
