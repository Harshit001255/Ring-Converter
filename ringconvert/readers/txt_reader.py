from ringconvert.document import Document

def read(input_path):
    with open(input_path, "r", encoding = "utf-8") as f:
        lines = f.read()

    doc = Document()
    for line in lines.splitlines():
        doc.add_paragraph(line)

    return doc