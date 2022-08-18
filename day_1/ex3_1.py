#!/usr/bin/env python3
from unittest import result


data = 9


def solve(input_data):
    """Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.

    Ví dụ::

      input_data = 5 # (0b101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    Hàm có sẵn tạo ra integer từ string: 69 == int('69')
    """
    
    result = bin(input_data)
    
    # code here
    
    print(f"input_data = {input_data} ({result})")
    print(f"output = {result[result.rfind('1'):]}")
    return result[result.rfind('1'):]
    

def main():
    print(solve(data))
    
if __name__ == "__main__":
    main()
