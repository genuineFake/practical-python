# bounce.py
#
# Exercise 1.5
height = 100
bounce_back = 0.60
count = 1

while count <= 10:
    print(count, round(height * bounce_back, 4))
    height *= bounce_back
    count += 1
