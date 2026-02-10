import sys
sys.stdin = open("flatten_input.txt", "r")


# for each test
for test_case in range(1, 11):

    N = int(input())
    boxes = list(map(int, input().split()))

    # N번만큼 반복
    for i in range(N):
    # find max and min
        max_boxes = max(boxes)
        min_boxes = min(boxes)
        boxes.remove(max_boxes)
        boxes.remove(min_boxes)
    # dump => max = max - 1, min = min + 1
        max_boxes -= 1
        min_boxes += 1
        boxes.append(max_boxes)
        boxes.append(min_boxes)

    # find final max and min
    # print difference
    print(f'#{test_case} {max(boxes) - min(boxes)}')