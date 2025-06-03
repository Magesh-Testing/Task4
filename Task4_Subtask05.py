#How can I use Python to find all the ways to make Rs. 10 using Rs. 1, Rs. 2, Rs. 5 and Rs. 10?
def n_ways_to_find_10():
    for a in range(11):
        for b in range(6):
            for c in range(3):
                for d in range(2):
                    if a + 2*b + 5*c + 10*d == 10:
                        print(f"Rs. 1 x {a}, Rs. 2 X {b}, Rs. 5 x {c}, Rs. 10 x {d}")

n_ways_to_find_10()