#!/usr/bin/env python3


def check_obj(obj, class_):
    return isinstance(obj, class_)

if __name__ == "__main__":
    class Base:
        pass


    b = Base()
    i = [1, 2]
    for x in [b, i]:
        if check_obj(x, int):
            print(f"{x} is from class {int.__name__}")
        if check_obj(x, list):
            print(f"{x} is from class {list.__name__}")
        if check_obj(x, Base):
            print(f"{x} is from class {Base.__name__}")
        if check_obj(x, object):
            print(f"{x} is from class {object.__name__}")

        print(f"{'':.^20}")