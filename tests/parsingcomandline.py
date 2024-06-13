"""
File to grab the ticker symbol from the command line
"""
import argparse

# Initialize the argument parser with a description
parser = argparse.ArgumentParser(description="Testing argument parsing")

# Add a command-line argument called 'smoke_test'
parser.add_argument("-smoke", action="store", dest="smoke_test")

# Parse the command-line arguments
command_line_arg = parser.parse_args()

# Print the value of the 'smoke_test' argument
lines = command_line_arg.smoke_test
print(lines)
