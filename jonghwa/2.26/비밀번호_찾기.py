import sys
input = sys.stdin.readline

N,M=map(int,input().split())

site_dict = {}

for _ in range(N):
    site,pw = input().split()
    site_dict[site] = pw

for _ in range(M):
    query_site = input().rstrip()
    print(site_dict[query_site])