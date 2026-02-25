import sys

def solve():
    # 빠른 입출력을 위한 설정
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    n = int(input[ptr])
    m = int(input[ptr+1])
    ptr += 2

    # Java의 1,000,001 크기 배열 대응
    pre = [0] * 1000001
    post = [0] * 1000001

    # 초기 배열 구성
    nodes = []
    for _ in range(n):
        nodes.append(int(input[ptr]))
        ptr += 1

    for i in range(n):
        curr_node = nodes[i]
        prev_node = nodes[i-1] # i=0일 때 nodes[-1]은 마지막 원소를 가리킴 (Python 특징)
        next_node = nodes[(i+1) % n]
        
        pre[curr_node] = prev_node
        post[curr_node] = next_node

    output = []

    # 명령어 처리
    for _ in range(m):
        cmd = input[ptr]
        i_node = int(input[ptr+1])
        ptr += 2
        
        pre_idx = pre[i_node]
        post_idx = post[i_node]

        if cmd == "BN":
            new_node = int(input[ptr])
            ptr += 1
            
            pre[new_node] = i_node
            post[new_node] = post_idx
            
            post[i_node] = new_node
            pre[post_idx] = new_node
            
            output.append(str(post_idx))

        elif cmd == "BP":
            new_node = int(input[ptr])
            ptr += 1
            
            post[new_node] = i_node
            pre[new_node] = pre_idx
            
            post[pre_idx] = new_node
            pre[i_node] = new_node
            
            output.append(str(pre_idx))

        elif cmd == "CN":
            # i_node의 다음 노드(post_idx)를 제거
            target = post_idx
            new_post = post[target]
            
            post[i_node] = new_post
            pre[new_post] = i_node
            
            output.append(str(target))

        elif cmd == "CP":
            # i_node의 이전 노드(pre_idx)를 제거
            target = pre_idx
            new_pre = pre[target]
            
            pre[i_node] = new_pre
            post[new_pre] = i_node
            
            output.append(str(target))

    # 한 번에 출력하여 속도 최적화
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()