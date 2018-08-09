import sys

# 算聊天列表排序
class PrintMemberList:
    def __init__(self):
        # 上下线权重10，身份权重1
        self.member_status = {}

if __name__ == "__main__":
    list_printer = PrintMemberList()

    member_num = int(sys.stdin.readline().strip())
    for i in range(member_num):
        line = list(sys.stdin.readline().split())
        list_printer.member_status[line[1]] = -int(line[0])

    operation_num = int(sys.stdin.readline().strip())
    for i in range(operation_num):
        line = list(sys.stdin.readline().split())
        if int(line[1]) == 1:
            list_printer.member_status[line[0]] -= 10
        elif int(line[1]) == 0:
            list_printer.member_status[line[0]] += 10
    sort_status_list = sorted(list_printer.member_status.items(), key=lambda x: (x[1], x[0]))
    for pair in sort_status_list:
        print(pair[0])






