# https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None
        self.pre = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add_first(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nxt = self.head
            self.head.pre = new_node
            self.head = new_node
        self.size += 1
        return new_node

    def add_last(self, element):
        new_node = Node(element)
        if self.tail is None:
            return self.add_first(element)
        new_node.pre = self.tail
        self.tail.nxt = new_node
        self.tail = new_node
        self.size += 1
        return new_node

    def insert_before(self, cursor, value):
        """cursor 바로 앞에 삽입"""
        if cursor is None:
            # 커서가 맨 끝 → 맨 뒤에 추가
            return self.add_last(value)
        if cursor is self.head:
            return self.add_first(value)

        new_node = Node(value)
        pre = cursor.pre
        new_node.nxt = cursor
        new_node.pre = pre
        pre.nxt = new_node
        cursor.pre = new_node
        self.size += 1
        return new_node

    def remove_before(self, cursor):
        """cursor 바로 앞 노드 삭제"""
        if cursor is None:
            # 커서가 맨 끝 → tail 삭제
            target = self.tail
        else:
            target = cursor.pre

        if target is None:
            return  # 삭제할 노드 없음

        pre = target.pre
        nxt = target.nxt

        if pre:
            pre.nxt = nxt
        else:
            self.head = nxt  # target이 head였음

        if nxt:
            nxt.pre = pre
        else:
            self.tail = pre  # target이 tail이었음

        self.size -= 1


st = input().rstrip()
n = int(input())

ll = LinkedList()
for ch in st:
    ll.add_last(ch)

cursor = None  # None = 커서가 맨 끝

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'L':
        if cursor is None:
            cursor = ll.tail       # 맨 끝 → tail로
        elif cursor is not ll.head:
            cursor = cursor.pre    # 한 칸 왼쪽
    elif cmd[0] == 'D':
        if cursor is not None:
            cursor = cursor.nxt    # None이면 이미 맨 끝
    elif cmd[0] == 'B':
        if cursor is ll.head:
            pass                   # 맨 앞이면 삭제 불가
        else:
            ll.remove_before(cursor)
            # cursor 자체는 그대로, 앞 노드만 사라짐
    else:  # P
        ll.insert_before(cursor, cmd[1])

result = []
cur = ll.head
while cur:
    result.append(cur.value)
    cur = cur.nxt

print(''.join(result))
