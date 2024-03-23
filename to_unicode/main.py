import argparse


def main():

    parser = argparse.ArgumentParser(description="parse string into unicode to reverse")
    parser.add_argument("-r", "--reverse", action="store_true", default=False, help="input unicode point and output strings")
    args = parser.parse_args()

    with open("./input", encoding="utf8") as input_file:
        content = input_file.read()

    if args.reverse:
        print("reverse from unicode points")
        with open("./output", "wt", encoding="utf8") as output:
            for line in content.split("\n"):
                arr = line.strip().split("\\u")
                convert_back = "".join(chr(int(hex_value, 16)) for hex_value in arr if hex_value)
                print(line)
                print(convert_back)
                print()
                output.write(convert_back)
                output.write("\n")
                output.write(line)
                output.write("\n")
                output.write("\n")

    else:
        print("convert into unicode points")
        with open("./output", "wt", encoding="utf8") as output:
            for line in content.split("\n"):
                s = "".join(r"\u{:04X}".format(ord(c)) for c in list(line))
                print(line)
                print(s)
                print()
                output.write(line)
                output.write("\n")
                output.write(s)
                output.write("\n")
                output.write("\n")


if __name__ == "__main__":
    main()
