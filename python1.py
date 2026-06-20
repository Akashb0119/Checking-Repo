import sys
import time

print("Hello world")
print("hello")
print("this is my project -monish")

message = "Monish is good developer"
colors = [31, 33, 32, 36, 34, 35]
for index, char in enumerate(message):
    color_code = colors[index % len(colors)]
    sys.stdout.write(f"\033[1;{color_code}m{char}\033[0m")
    sys.stdout.flush()
    time.sleep(0.05)
print("hello bmonish")
print("hello bakash")