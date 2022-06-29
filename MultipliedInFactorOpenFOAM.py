import pandas as pd

def main():
    file = open("./U", "r")
    lines = file.readlines()
    new_lines = []
    line_start = 22
    line_end = 1117876

    factor = 86400

    header = lines[:line_start]
    footer = lines[line_end+1:]

    for line in lines[line_start:line_end+1]:
        vel = [factor * float(nr) for nr in line.replace("(", "").replace(")\n", "").split(" ")]
        new_lines.append(f"({vel[0]} {vel[1]} {vel[2]})\n")

    fout = open("test.out", "w")
    fout.writelines(header+new_lines+footer)
    fout.close()




if __name__ == "__main__":
    main()
