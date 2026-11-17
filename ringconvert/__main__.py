import sys
import zipfile
from ringconvert.router import convert

if len(sys.argv) != 3:
    print("Usage: python3 -m ringconvert <input_file> <output_extension>")
    sys.exit(1)

input_path = sys.argv[1]
target_ext = sys.argv[2]
try:
    output_path = convert(input_path, target_ext)
    print(f"saved: {output_path}")
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
except FileNotFoundError:
    print(f"Error: file not found: {input_path}")
    sys.exit(1)
except zipfile.BadZipFile:
    print("Error: not a valid .docx file:", input_path)
    sys.exit(1)