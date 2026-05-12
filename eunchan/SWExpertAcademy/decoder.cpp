#include <cstdio>
const int BLOCK = 32;
const int X = 2048;
const int Y = 2048;
const int TOTAL_BLOCK = 64 * 64;
const int PUZZLE = 64;

struct Info {
	unsigned int up, down, left, right;
	bool check_up, check_down, check_left, check_right;
};

static void swap(char bitmap[][X], int puzzle_a, int puzzle_b)
{
	int sx, sy, dx, dy;
	sx = 32 * (puzzle_a % PUZZLE);
	sy = 32 * (puzzle_a / PUZZLE);
	dx = 32 * (puzzle_b % PUZZLE);
	dy = 32 * (puzzle_b / PUZZLE);
	for (register int y = 0; y < BLOCK; y++)
		for (register int x = 0; x < BLOCK; x++)
		{
			register int t = bitmap[sy + y][sx + x];
			bitmap[sy + y][sx + x] = bitmap[dy + y][dx + x];
			bitmap[dy + y][dx + x] = t;
		}
}

int find_right(char bitmap[][X], int i, int j, Info* puzzle_info) {
	int count = 0;
	int id = 64 * i + j;
	puzzle_info[id].check_right =
	puzzle_info[id].check_left =
	puzzle_info[id].check_down =
	puzzle_info[id].check_up = false;
	// 외곽선은 무조건 일치하는 것으로 간주 (기존 로직 유지)
	if (i == 0 || i == 63) {
		count++;
		if (i == 0) puzzle_info[id].check_left = true;
		if (i == 63) puzzle_info[id].check_right = true;
	}
	if (j == 0 || j == 63) {
		count++;
		if (j == 0) puzzle_info[id].check_up = true;
		if (j == 63) puzzle_info[id].check_down = true;

	}

	// 상하좌우: 이웃이 범위 내에 있을 때만 비트 비교
	if (i > 0 && puzzle_info[id].up == puzzle_info[id - 64].down) {
		count++; // Up
		puzzle_info[id].check_up = true;
	}
	if (i < 63 && puzzle_info[id].down == puzzle_info[id + 64].up) {
		count++; // Down
		puzzle_info[id].check_down = true;
	}
	if (j > 0 && puzzle_info[id].left == puzzle_info[id - 1].right) {
		count++; // Left
		puzzle_info[id].check_left = true;
	}
	if (j < 63 && puzzle_info[id].right == puzzle_info[id + 1].left) {
		count++; // Right
		puzzle_info[id].check_right = true;
	}
	return count;
}

void test(char bitmap[][X])
{
	// 64 * 64의 puzzle map이 bitmap으로 들어옴.
	//set puzzle_info
	Info* puzzle_info = new Info[PUZZLE*PUZZLE];
	//init
	for (int i = 0; i < PUZZLE*PUZZLE; i++) {
		puzzle_info[i].up =
		puzzle_info[i].down =
		puzzle_info[i].left = 
		puzzle_info[i].right = 0U;
	}

	//퍼즐을 돌면서 각 퍼즐의 경계 값을 검색.
	for (int i = 0; i < PUZZLE; i++) {
		for (int j = 0; j < PUZZLE; j++) {
			for (int a = i * 32; a < i * 32 + 32; a++) {
				for (int b = j * 32; b < j * 32 + 32; b++) {
					if (a % 32 == 0 && bitmap[a][b]) puzzle_info[64 * i + j].up |= (1U << (b%32));
					if (a % 32 == 31 && bitmap[a][b]) puzzle_info[64 * i + j].down |= (1U << (b%32));
				}
				if (bitmap[a][j*32]) puzzle_info[64 * i + j].left |= (1U << (a%32));
				if (bitmap[a][j*32+31]) puzzle_info[64 * i + j].right |= (1U << (a%32));
			}
		}
	}
	// 각 퍼즐의 제자리가 현 위치라고 생각하고,
	// 일단 위아래가 안맞는지를 확인해서 print 해보자.
	char** true_map = new char*[64];
	int* false_idx = new int[1000];
	int tmp = 0;
	for (int i = 0; i < PUZZLE; i++) true_map[i] = new char[64];
	for (int i = 0; i < PUZZLE; i++) {
		for (int j = 0; j < PUZZLE; j++) {
			int count = find_right(bitmap, i, j, puzzle_info);
			true_map[i][j] = count;
			if (count < 3) false_idx[tmp++] = 64*i+j;
		}
	}
	// 퍼즐의 진리표 완성.
	tmp--;
	for (int i = 0; i < PUZZLE; i++) {
		for (int j = 0; j < PUZZLE; j++) {
			if (true_map[i][j] < 4) {
				for (int dir = 0; dir < 4; dir++) {
					puzzle_info[64*i+j]
					for (int k = 0; k < tmp; k++) {

					}
				}
			}
		}
	}
    // 퍼즐을 다시 제자리로 변경해야하는 로직 구현해야함.
	//memory 해제
	for (int i = 0; i < PUZZLE; i++) delete[] true_map[i];
	delete[] true_map;
	delete[] puzzle_info;
	delete[] false_idx;
}
