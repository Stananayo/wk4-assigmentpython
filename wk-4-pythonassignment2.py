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
        print(f"Error: The file '{input_filename}' does not exist. Please check the file name and try again.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}' or write to '{output_filename}'.")

def main():
    while True:
        # Ask the user for the input filename
        input_filename = input("Please enter the name of the file to read from: ")
        # Ask for the output filename
        output_filename = input("Please enter the name of the file to write to: ")

        # Try to read and modify the file
        if read_and_modify_file(input_filename, output_filename):
            break  # If successful, exit the loop

if __name__ == "__main__":
    main()
# The code above is a Python script that reads a file, modifies its content by converting all lines to uppercase, and writes the modified content to a new file. It includes error handling for file not found and IO errors. The main function prompts the user for input and output filenames and calls the read_and_modify_file function.
# The script will continue to prompt the user until a valid file is processed successfully.
