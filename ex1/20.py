import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
sum = int(arg1) + int(arg2)
if sum >= 80 and sum < 90:
    print("OK")
elif sum >= 90:
    print("GOOD")
else:
    print("NG")