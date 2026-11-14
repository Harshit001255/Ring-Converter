import zipfile
import xml.etree.ElementTree as ET
from ringconvert.document import Document

url = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def read(input_path):
    with zipfile.ZipFile(input_path) as z:
        data = z.read("word/document.xml")

    root = ET.fromstring(data)

    doc = Document()
    for item in root.iter("{"+url+"}p"):
        para_text = ""
        for t in item.iter("{"+url+"}t"):
            if t.text != None:
                para_text += t.text
        doc.add_paragraph(para_text)

    return doc    