from ringconvert.readers import docx_reader
from ringconvert.writers import txt_writer
from ringconvert.readers import txt_reader
from ringconvert.writers import html_writer

READERS = {
    "docx": docx_reader.read,
    "txt": txt_reader.read
}

WRITERS = {
    "txt": txt_writer.write,
    "html": html_writer.write
}

def get_reader(ext):
    if ext in READERS:
        return READERS[ext]
    else:
        raise ValueError(f"No reader found for {ext} files.")

def get_writer(ext):
    if ext in WRITERS:
        return WRITERS[ext]
    else:
        raise ValueError(f"No writer found for {ext} files.")