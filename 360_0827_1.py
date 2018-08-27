#coding=utf-8
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    input_data = []
    for _ in range(n):
        input_data.append(list(map(int, input().split(" "))))
    width_range = [input_data[i][0] for i in range(n)]
    height_range = [input_data[i][1] for i in range(n)]
    width = max(width_range) - min(width_range)
    height = max(height_range) - min(height_range)
    print(max(width, height) ** 2)

