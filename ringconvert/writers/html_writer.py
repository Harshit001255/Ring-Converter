import html

def write(document, output_path):
    parts = []
    parts.append("<!DOCTYPE html>")
    parts.append("<html>")
    parts.append("<head>")
    parts.append('<meta charset="utf-8">')
    parts.append("<title>Document</title>")
    parts.append("</head>")
    parts.append("<body>")
    for para in document.paragraphs:
        parts.append("<p>" + html.escape(para) + "</p>")
        parts.append("</body>")
        parts.append("</html>")


    with open(output_path, "w", encoding = "utf-8") as f:
        f.write("\n".join(parts))

