import argparse

parser = argparse.ArgumentParser(description="testing argues")

parser.add_argument('-smoke', action="store", dest="smoke_test")

command_line_arg = parser.parse_args()

if command_line_arg.smoke_test == 'hi':
    print("haaaaaaa")

else:
    print("mean line")

lines = command_line_arg.smoke_test
print(lines)
