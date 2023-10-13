# Define file paths
input_file = "input.txt"
output_file = "output.txt"

# Read from the input file and write to the output file
try:
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            # Process the line (e.g., manipulate or transform it)
            # For this example, we'll just write it to the output file
            outfile.write(line)

    print("File read and write completed successfully.")
except IOError as e:
    print(f"An error occurred: {e}")
