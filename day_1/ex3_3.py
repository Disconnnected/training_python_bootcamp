#!/usr/bin/env python3

"""
In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ “Fizz”
thay vì số đo. Với bội của 5, in ra chữ “Buzz” thay vì số đó. Với các số là bội
của cả 3 và 5 thì in ra chữ “FizzBuzz” thay vì số đó. Các số còn lại thì in ra
bình thưòng.
"""


def solve():
    """Thay vì in ra, hãy trả về 1 `list`
    100 phần tử thỏa mãn yêu cầu đề bài

    :rtype: list
    """
    list_100 = []
    for n in range(1,101):
        if (n%3 == 0 and n%5 == 0):
            list_100.append("FizzBuzz")
        elif (n%5 == 0):
            list_100.append("Buzz")
        elif (n%3 == 0 ):
            list_100.append("Fizz")
        else:
            list_100.append(n)
    print(list_100)
    result = None


    return result


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()
