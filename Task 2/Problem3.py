
pattern = input()

com = ""

for ch in pattern:
    if ch == "A":
        com += "T"
    elif ch == "T":
        com += "A"
    elif ch == "C":
        com += "G"
    elif ch == "G":
        com += "C"

reverse_complement = com[::-1]

print(reverse_complement)
