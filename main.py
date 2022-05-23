from docx import Document
from htmldocx import HtmlToDocx


document = Document()
new_parser = HtmlToDocx()

# do stuff to document
html = '<h1>Hello world</h1>'
new_parser.add_html_to_document(html, document)

# do more stuff to document
document.save('your_file_name.docx')