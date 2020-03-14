import camelot
from PyPDF2 import PdfFileReader as pdr

tables = camelot.read_pdf("data.pdf", flavor = 'stream')
print(tables)

