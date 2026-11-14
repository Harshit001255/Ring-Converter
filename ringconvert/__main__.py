import sys
from ringconvert.router import convert

if len(sys.argv) != 3:
    print("Usage: python3 -m ringconvert <input_file> <output_extension>")
    sys.exit(1)

input_path = sys.argv[1]
target_ext = sys.argv[2]

output_path = convert(input_path, target_ext)
print(f"saved: {output_path}")