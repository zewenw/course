# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

from Employee import Employee


def print_hi(name):
    emp = Employee(
        'jack',
        15,
        'jack@litets.com'
    )

    print('dict：', emp)

    person_json = json.dumps(emp.__dict__)  # 转换为json

    print('json：', person_json)

    print(emp.__getattribute__('age'))


def count_bit_twins(num_str):
    num = int(num_str)
    binary = "{0:032b}".format(num) # convert to 32-bit binary string
    count = 0
    for i in range(30):
        if binary[i:i+4] == "0110":
            count += 1
    print(count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count_bit_twins(6)
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
