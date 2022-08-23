#!/usr/bin/env python3

"""
a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

Ví dụ:

- output: [[9, 1, 1], ...]
"""


from tracemalloc import start


def solve():
    """Trả về list chứa các list là các bộ số thỏa mãn đề bài

    Ví dụ:
        [[9, 1, 1], ..., [1, 9, 1]]

    Lưu ý: kết quả từng list con trả về với a giảm dần, b và c tăng dần
    """

    
    result = []
    # a, b, c = map(int,input("nhập 3 số tự nhiên:").split()) 
    # for i in range(1,10):
    #     lst = []
    #     for j in range(3):
    #         elemt = i-j
    #         print(lst)
    #         if (lst[1] + lst[2]/lst[3] == 10):
    #             lst.append(elemt)
    #     result.append(lst)
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
