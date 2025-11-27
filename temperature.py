import sys

if len(sys.argv) == 2:
    temp = float(sys.argv[1])
else:
    print("No temperature entered. Using default temperature...")
    temp = 28.0  # default temperature

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")
