from PyPDF4 import PdfFileReader, PdfFileWriter
from pathlib import Path

pdf_writer = PdfFileWriter()
source_pdf_0 = PdfFileReader('/dev/shm/tmp1.pdf')
source_pdf_1 = PdfFileReader('/dev/shm/tmp1.pdf')

page_0 = source_pdf_0.getPage(0).rotateClockwise(90)
pdf_writer.addPage(page_0)
page_1 = source_pdf_1.getPage(0).rotateCounterClockwise(90)
pdf_writer.addPage(page_1)

new_pdf = Path('/dev/shm/new.pdf')
with new_pdf.open(mode='wb') as new_pdf_file:
    pdf_writer.write(new_pdf_file)
