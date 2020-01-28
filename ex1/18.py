import sys

if len(sys.argv) < 2:
    sys.exit("Less agument.")

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print("1st:" +str(arg1))
print("2st:" +str(arg2))