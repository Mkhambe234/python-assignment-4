def read_and_modify_file(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"File successfully processed. Modified content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
input_filename = input("Enter the input filename: ")
output_filename = input("Enter the output filename: ")
read_and_modify_file(input_filename, output_filename)