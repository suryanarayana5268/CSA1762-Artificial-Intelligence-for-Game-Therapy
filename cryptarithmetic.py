import itertools
def solve_cryptarithmetic():
    for perm in itertools.permutations(range(10),8):  # Generate all permutations of digits for 8 unique letters
        # Unpack the digits from the permutation
        s, e, n, d, m, o, r, y = perm

        # Check if the digits satisfy the equation SEND + MORE = MONEY
        if s and m and (s * 1000 + e * 100 + n * 10 + d) + (
                m * 1000 + o * 100 + r * 10 + e) == m * 10000 + o * 1000 + n * 100 + e * 10 + y:
            # If valid, print the solution with the corresponding digits
            print(f"SEND={s}{e}{n}{d}, MORE={m}{o}{r}{e}, MONEY={m}{o}{n}{e}{y}")
            break  # Exit the loop after finding the first solution
solve_cryptarithmetic()
