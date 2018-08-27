#coding=utf-8
# 29%
def get_type_num(array, type_num, st_time, end_time):
    if end_time < st_time:
        return 0
    visit_record = [0] * type_num
    for _ in range(st_time-1, end_time):
        if visit_record[array[_]-1] == 0:
            visit_record[array[_]-1] = 1
    return sum(visit_record)

if __name__ == "__main__":
    n_len, m_type = list(map(int, input().split(" ")))
    input_data = list(map(int, input().split(" ")))
    ques_num = int(input())
    for _ in range(ques_num):
        query = list(map(int, input().split(" ")))
        print(get_type_num(input_data, m_type, query[0], query[1]))
