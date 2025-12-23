# Differnece between for and while loop
```
k = 2
n = 10

for x in range(1, n, k):
    print(x)
    x = 100  # x is set equal to 100
    print(x)
```
for this the output is 1 100 3 100 5 100 7 100 9 100\
for loop don't cares about the assigned value for x in the loop

```
k = 2
n = 10
x = 1

while x < n:
    print(x)
    x = 100  # Now this will actually affect the "x < n" check
    print(x)
    # The loop will check: Is 100 < 10? No. 
    # It stops immediately.
```

for this the output is 1 100
