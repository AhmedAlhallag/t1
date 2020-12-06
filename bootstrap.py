# Driver
from searching import Searching
import time

sObj = Searching()

d = {
    1: "CHECK SUBSTRING",
    2: "SORT A GIVEN LIST"
}


def print_d(d):
    for k, v in d.items():
        print(f"[{k}]: {v}")


rep = None

while rep != "exit":
    time.sleep(0.5)
    print("Choose a number from the menu: ")
    print_d(d)
    rep = int(input("> "))  # key
    if rep == 1:
        s = input("Enter a string: ")
        sub = input("Enter a sub-string: ")
        sObj.set_string_sub(s, sub)
        match = sObj.subString()
        if match:
            print("THERE IS A MATCH!")
        else:
            print("THERE IS NO MATCH!")
    elif rep == 2:
        pass
    else:
        print("UNKOWN COMMAND.")
