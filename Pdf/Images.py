from pikepdf import Pdf, Name, PdfImage

old_pdf = Pdf.open("A.pdf")
page_1 = old_pdf.pages[0]
# print(list(page_1.images.keys()))
# ['/X6']

extract_image = page_1.images['/X6']
pdf_image = PdfImage(extract_image)
pdf_image.extract_to(fileprefix="img")