def write(document, output_path):
    string = ("\n".join(document.paragraphs))
    with open(output_path, "w", encoding = "utf-8") as f:
        f.write(string)