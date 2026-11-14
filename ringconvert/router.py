import os
from ringconvert.registry import get_reader, get_writer

def convert(input_path, target_ext):
    base, ext = os.path.splitext(input_path)
    e = ext.lower()
    te = target_ext.lower()
    te = te.lstrip(".")

    reader = get_reader(e.lstrip("."))
    doc = reader(input_path)

    writer = get_writer(te)

    output_path = base + "." + te
    counter = 1
    while os.path.exists(output_path):
        output_path = base + "_" +str(counter) + "." + te
        counter += 1

    writer(doc, output_path)
    return output_path