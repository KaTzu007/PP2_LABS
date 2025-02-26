import time
import math

print("Sample Input:")

num = int(input())
miliseconds = int(input())
seconds = miliseconds / 1000 #Changed miliseconds into seconds because function sleep works with seconds
time.sleep(seconds)

print("Sample Output:")
print(f"Square root of {num} after {miliseconds} miliseconds is {math.sqrt(num)}")