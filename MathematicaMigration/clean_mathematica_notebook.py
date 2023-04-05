input_file = "inputs.txt"
output_file = "cleaned_output.txt"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:
        if not line.startswith("Out["):
            outfile.write(line)

