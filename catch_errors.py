###how to catch errors in python
import sys

filename = "inputs.txt"

try:
    print("INSIDE TRY")
    myfile = open(filename, mode="r", encoding="utf-8")
except Exception:
    print("INSIDE EXCEPT")
    print(sys.exc_info()[1])### to show error
else:
    print("INSIDE ELSE")
    print(myfile.read())
finally:
    print("INSIDE FINALLY")
    print("TASK IS OVER")
