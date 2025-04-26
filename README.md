# File Read and Modify Script

## Overview

This Python script reads the contents of a specified input file, modifies the content by transforming all lines to uppercase, and writes the modified content to a new output file. The program includes error handling to manage scenarios where the specified input file does not exist or cannot be accessed.

## Features

- Reads content from a user-specified input file.
- Modifies content by converting all text to uppercase.
- Writes the modified content to a user-specified output file.
- Implements error handling for file operations.

## Requirements

- Python 3.x installed on your system.

## Usage

1. **Clone the repository or download the script**.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:
4. When prompted, enter the name of the input file you want to read from (make sure the file exists in the same directory).
5. Enter the desired name for the output file where the modified content will be saved.

## Error Handling
- The program will handle the following errors:
- FileNotFoundError: If the specified input file does not exist, an appropriate error message will be displayed.
- IOError: If there are issues reading the input file or writing to the output file, an appropriate error message will be displayed.
- Example: If you have an input file named example.txt containing:
 (  Hello, World!
This is a test file.)
- After running the script and inputting example.txt as the input file and output.txt as the output file, output.txt will contain:
(HELLO, WORLD!
THIS IS A TEST FILE.)

## File Read & Write Program with Error Handling
def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read contents from the input file
            content = infile.readlines()

        # Example modification: Convert all lines to uppercase
        modified_content = [line.upper() for line in content]

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}' or write to '{output_filename}'.")

def main():
    # Ask the user for the input filename
    input_filename = input("Please enter the name of the file to read from: ")
    # Ask for the output filename
    output_filename = input("Please enter the name of the file to write to: ")

    # Call the function to read and modify the file
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()

   
   ```Stan
   wk4-assignmentpython.py
