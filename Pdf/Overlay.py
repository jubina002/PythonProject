from pikepdf import Pdf, Page, Rectangle

old_pdf1 = Pdf.open("A.pdf")
old_pdf2 = Pdf.open("pm.pdf")
destination_page = Page(old_pdf1.pages[0])
source_page = Page(old_pdf2.pages[0])

destination_page.add_overlay(source_page, Rectangle(0,0,500,500))
old_pdf1.save("NewPdf.pdf")
#A ma pm overlay