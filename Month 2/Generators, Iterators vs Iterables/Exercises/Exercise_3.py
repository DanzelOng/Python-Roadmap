# Generator Exercise - 1
# Write a program to generate the first 10 numbers of the Fibonacci sequence.
def getFibo10():
    n, a, b = 1, 1, 1
    if n == 1:
        yield a
        n += 1
    if n == 2:
        yield a
        n += 1
    for _ in range(2, 10):
        a, b = b, a + b
        yield b

gen = getFibo10()
for g in gen:
    print(g)