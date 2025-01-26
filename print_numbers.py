n = 10
t1, t2 = 0, 1

print("Fibonacci Series:", end=" ")
for i in range(1, n + 1):
    if i == 1:
        print(t1, end=" ")
        continue
    if i == 2:
        print(t2, end=" ")
        continue
    next_term = t1 + t2
    t1 = t2
    t2 = next_term
    print(next_term, end=" ")
