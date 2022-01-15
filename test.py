ignore = ["duplex", "alias", "configuration"]

with open("config_sw1.txt") as f:
    for line in f:
        words = line.split()
        line_x = set(words) & set(ignore)
        if not line.startswith("!") and not line_x:
            print(line.rstrip())

