#!/usr/bin/env python3

"""
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
"""


import calendar


def solve(input_data):
    """Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    (1,2) là biểu diễn tương tự [1,2], chỉ thay dấu ngoặc vuông thành tròn.
    Đây là kiểu dữ liệu tuple.
    :param input_data: tháng bất kì
    :rtype: list
    """
    result = int(input())
    name = list(calendar.month_name)
    del name[0]   ###delete space
    lst_month = list(enumerate(name,start=1))

    ### add day
    for i in range(1,13): 
        if (i == 2):
            lst_month[i-1] += (28,)
        elif (i%2 == 1):
            lst_month[i-1] += (30,)
        else:
            lst_month[i-1] += (31,)
    # print(lst_month)

    ###tuple to list
    change_to_list = [list(j) for j in lst_month]
    for x in change_to_list: ### remove enumrate
        x.pop(0)
    # print(change_to_list)
    
    ###list to tuple
    change_to_tuple = tuple(tuple(y) for y in change_to_list)
    # print(change_to_tuple)
    
    ### nhập tháng và in ra
    for z in range(1,13):
        if (z == result):
            print(change_to_tuple[z-1])
    
    return result
def main():
    month, day = solve(0)
    print(month, day)


if __name__ == "__main__":
    main()
