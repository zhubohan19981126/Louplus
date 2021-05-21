#!/usr/bin/env python3
for i in range(1, 101):
    a = i % 7
    b = i % 10
    c = i // 10
    if a == 0 or b == 7 or c == 7:
        continue
    else:
        print(i)
