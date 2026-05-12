// C형 준비 문제
// 1. 쓰레기를 기본적으로 처리하는데 성공했지만, 쓰레기가 조금씩 남는 문제가 있음.
// usercode.cpp
#include <malloc.h>
#include <cstdio>

struct Pos {
	int r, c;
};

struct trash_Pos {
	int r, c, cost;
};

struct Queue {
	Pos* data;
	int front, rear;
	int qsize;
	void init(int size) {
		data = (Pos*)malloc(sizeof(Pos) * size);
		front = rear = 0;
		qsize = size;
	}

	void push(Pos p) {
		data[rear] = p;
		rear = (rear + 1) % qsize;
	}
	Pos pop() {
		Pos tmp = data[front];
		front = (front + 1) % qsize;
		return tmp;
	}
	bool is_empty() {
		return front == rear;
	}

	void clear() {
		free(data);
	}
};

void sort(trash_Pos *p) {
	for (int i = 9999; i >= 0; i--) {
		for (int j = 0; j < i; j++) {
			if (p[j].cost > p[j+1].cost) {
				trash_Pos tmp = p[j];
				p[j] = p[j + 1];
				p[j + 1] = tmp;
			}
		}
	}
}

void move_trash(int y, int x, int d);
/* x, y = 쓰레기 위치, d = 쓰레기통 방향*/
void test(int trash_map[1000][1000])
{
	printf("test start");
	Queue q;
	int trash_can[3] = { 0, };
	q.init(1000 * 1000);
	// visit 배열
	int **visit = (int **)malloc(sizeof(int*) * 1000);
	for (int i = 0; i < 1000; i++) {
		*(visit+i) = (int *)malloc(sizeof(int) * 1000);
	}
	// cost 배열
	trash_Pos *trash = (trash_Pos*)malloc(sizeof(trash_Pos) * 10000);
	int k = 0;
	// 쓰레기통 위치 탐색
	for (int i = 0; i < 1000; i++) {
		for (int j = 0; j < 1000; j++) {
			visit[i][j] = 0;
			// 쓰레기통을 만나면,
			if (trash_map[i][j] > 0) {
				visit[i][j] = 1;
				q.push({ i, j });
			}
		}
	}
	printf("find trash can finish\n");
	// c로 bfs 구현 어케 하는건데,,,
	int tp = 0; // trash position
	printf("bfs start\n");
	while (!q.is_empty()) {
		// 시작점. 쓰레기통.
		Pos now;
		now = q.pop();
		// bfs로 탐색하면서 visit에 비용을 구함.
		for (int i = 0; i < 4; i++) {
			int ox = now.c, oy = now.r;
			int x = now.c, y = now.r;
			switch (i)
			{
			case 0: y++; break;
			case 1: y--; break;
			case 2: x++; break;
			case 3: x--; break;
			}
			if ((x < 0) || (x >= 1000) || (ox < 0) || (ox >= 1000)) continue;
			if ((y < 0) || (y >= 1000) || (oy < 0) || (oy >= 1000)) continue;
			if (visit[y][x] != 0) continue;
			visit[y][x] = visit[oy][ox] + 1;
			q.push({ y,x });
			if (trash_map[y][x] == -1) {
				trash[tp] = { y,x,visit[y][x] };
				tp++;
			}
		}
	}
	printf("bfs finish\n");
	// 쓰레기가 어디에 있는지 다 구함.
	printf("sort start\n");
	sort(trash);
	printf("sort finish\n");
	// trash cost 기준으로 정렬 완료.
	int dx[4] = { 0,0,-1,1 };
	int dy[4] = { -1,1,0,0 };
	printf("throw away trash start\n");
	for (int i = 0; i < tp; i++) {
		//쓰레기가 쓰레기통에 들어갈 때까지
		int x = trash[i].c, y = trash[i].r;
		while (visit[y][x] > 1) {
			for (int j = 0; j < 4; j++) {
				int nx = x + dx[j], ny = y + dy[j];
				if ((nx < 0) || (nx >= 1000) || (ny < 0) || (ny >= 1000)) continue;
				if (visit[y][x] - visit[ny][nx] == 1) {
					move_trash(y, x, j);
					x = nx, y = ny;
					break;
				}
			}
		}
	}
	printf("throw away trash finish\n");
		// trash map 의 dx, dy에 쓰레기가 존재한다면,
		// 해당 위치에서 쓰레기통의 위치까지 간 경로를 기반으로
		// 역계산을 이용. 쓰레기를 버림.a
		// 모든 쓰레기를 버릴때까지 반복
	q.clear();
	free(trash);
	for (int i = 0; i < 1000; i++) {
		free(visit[i]);
	}
	free(visit);
	return;
}

// main.cpp
#include <cstdio>
#include <ctime>

using namespace std;

void test(int trash_map[1000][1000]);

static int seed = 3;  // the seed will be changed
static int result = 0;
static int dummy0[222];
static int trash_map[1000][1000];
static int dummy1[333];
static int ori_trash_map[1000][1000];
static int dummy2[444];
static int trash_can[3];

static int pseudo_rand(void)
{
	seed = seed * 214013 + 2531011;
	return (seed >> 16) & 0x7FFF;
}

static void build_map(void)
{
	for (int y = 0; y < 1000; y++)
		for (int x = 0; x < 1000; x++)
			trash_map[y][x] = 0;

	for (int c = 0; c < 10000;)
	{
		int x = pseudo_rand() % 1000;
		int y = pseudo_rand() % 1000;

		if (trash_map[y][x] == 0)
		{
			trash_map[y][x] = -1; // trash
			c++;
		}
	}

	for (int c = 1; c <= 3;)
	{
		int x = pseudo_rand() % 1000;
		int y = pseudo_rand() % 1000;

		if (trash_map[y][x] == 0)
		{
			trash_map[y][x] = c; // trash_can
			c++;
		}
	}

	trash_can[0] = trash_can[1] = trash_can[2] = 0;

	for (int y = 0; y < 1000; y++)
		for (int x = 0; x < 1000; x++)
			ori_trash_map[y][x] = trash_map[y][x];
}

void move_trash(int y, int x, int d)
{
	if (result == 1000000000) return;

	result++;

	int ox = x;
	int oy = y;

	switch (d)
	{
	case 0: y--; break;
	case 1: y++; break;
	case 2: x--; break;
	case 3: x++; break;
	}

	if ((x < 0) || (x >= 1000) || (ox < 0) || (ox >= 1000)) return;
	if ((y < 0) || (y >= 1000) || (oy < 0) || (oy >= 1000)) return;

	if (ori_trash_map[y][x] == -1 || ori_trash_map[oy][ox] != -1) return;
	// oy, ox는 쓰레기, y, x는 깨끗한 땅 or 쓰레기통
	if (ori_trash_map[y][x] == 0) // 깨끗한 땅이면
	{
		ori_trash_map[oy][ox] = 0;
		ori_trash_map[y][x] = -1; // 쓰레기 이동
	}
	else // 쓰레기통이면
	{ 
		int i = ori_trash_map[y][x] - 1; // 쓰레기통 번호

		if (trash_can[i] == 3500) // 1개 쓰레기통에 3500개씩 버릴 수 있음.
			return; // 최댓값을 넘어가면 함수 호출하면 안됨.

		ori_trash_map[oy][ox] = 0; // 쓰레기 버림.
		trash_can[i]++;
	}
	// 가까운 쓰레기통부터 처리해야..
}

int main(void)
{


	for (register int T = 0; T < 10; T++)
	{
		build_map();

		time_t START = clock();
		test(trash_map);
		result += ((clock() - START) / (CLOCKS_PER_SEC / 1000));
		int remain_trash = 0;
		for (int y = 0; y < 1000; y++)
			for (int x = 0; x < 1000; x++)
				if (ori_trash_map[y][x] == -1) {
					result += 10000;
					remain_trash++;
				}
		printf("remain_trash = %d\n", remain_trash);
	
	}
	if (result <= 43, 000, 000) {
		printf("PASS\n");
	}
	else {
		printf("FAIL\n");
	}
	printf("RESULT : %d\n", result);

	return 0;
}