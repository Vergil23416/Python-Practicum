input_file = input()
evens_file = input()
odds_file = input()
equals_file = input()
with open(input_file, encoding="UTF-8") as f:
    lines = [line for line in f if line.strip()]

even_set, odd_set = set("02468"), set("13579")
even, odd, eq = [], [], []
for line in lines:
    line_even, line_odd, line_eq = [], [], []
    for num in line.split():
        evens_count = sum(1 for c in num if c in even_set)
        odds_count = sum(1 for c in num if c in odd_set)

        if evens_count > odds_count:
            line_even.append(num)
        elif evens_count < odds_count:
            line_odd.append(num)
        else:
            line_eq.append(num)
    even.append(" ".join(line_even) + "\n")
    odd.append(" ".join(line_odd) + "\n")
    eq.append(" ".join(line_eq) + "\n")
with open(evens_file, "w", encoding="UTF-8") as f:
    f.writelines(even)
with open(odds_file, "w", encoding="UTF-8") as f:
    f.writelines(odd)
with open(equals_file, "w", encoding="UTF-8") as f:
    f.writelines(eq)
