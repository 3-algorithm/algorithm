/*
    BFS and Search All

    N x M grid starts at (0, 0).
    Each cell has a 1-based address:
    1  2  3  4  5
    6  7  8  9 10

    Given required addresses P, return the shortest path length needed to
    visit every required address starting from (0, 0).
*/
#include <algorithm>
#include <cstdlib>
#include <limits>
#include <vector>

using namespace std;

namespace {
vector<int> to_position(int address, int M) {
    int zero_based = address - 1;
    return {zero_based / M, zero_based % M};
}

int manhattan_distance(const vector<int>& a, const vector<int>& b) {
    return abs(a[0] - b[0]) + abs(a[1] - b[1]);
}
}  // namespace

int solution(int N, int M, vector<int> P) {
    (void)N;

    if (P.empty()) {
        return 0;
    }

    vector<vector<int>> positions;
    positions.push_back({0, 0});
    for (int address : P) {
        positions.push_back(to_position(address, M));
    }

    int required_count = static_cast<int>(P.size());
    vector<vector<int>> dist(required_count + 1, vector<int>(required_count + 1, 0));
    for (int i = 0; i <= required_count; ++i) {
        for (int j = i + 1; j <= required_count; ++j) {
            dist[i][j] = manhattan_distance(positions[i], positions[j]);
            dist[j][i] = dist[i][j];
        }
    }

    const int inf = numeric_limits<int>::max() / 4;
    int full_mask = (1 << required_count) - 1;
    vector<vector<int>> dp(1 << required_count, vector<int>(required_count, inf));

    for (int i = 0; i < required_count; ++i) {
        dp[1 << i][i] = dist[0][i + 1];
    }

    for (int mask = 1; mask <= full_mask; ++mask) {
        for (int current = 0; current < required_count; ++current) {
            if ((mask & (1 << current)) == 0 || dp[mask][current] == inf) {
                continue;
            }

            for (int next = 0; next < required_count; ++next) {
                if (mask & (1 << next)) {
                    continue;
                }

                int next_mask = mask | (1 << next);
                int next_cost = dp[mask][current] + dist[current + 1][next + 1];
                dp[next_mask][next] = min(dp[next_mask][next], next_cost);
            }
        }
    }

    return *min_element(dp[full_mask].begin(), dp[full_mask].end());
}
